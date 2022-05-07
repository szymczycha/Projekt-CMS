<script>
    let articleId = getParameterByName("id");
    let articlePageData;
    let currentArticle;
    let headerData;
    let footerData;
    let slideInterval;
    async function getarticlePageData() {
        const res = await fetch("/getMainPageData");
        articlePageData = await res.json();
        console.log(articlePageData);

        if (articlePageData.news.length == 0) {
            currentArticle = {
                header: "Placeholder header",
                title: "Placeholder title",
                content: "Placeholder content",
                buttonText: "Placeholder text",
                id: articleId,
                article: "Placeholder article",
            };
        } else
            currentArticle = articlePageData.news.find(
                (article) => article.id == articleId
            ) ?? {
                header: "Article not found",
                title: "Sorry, we couldn't find an article with the given id",
                content: "placeholder",
                buttonText: "placeholder",
                id: articleId,
                article: "placeholder",
            };

        if (articlePageData.headerItems.length == 0) {
            headerData = [
                { item: "Home" },
                { item: "Features" },
                { item: "Pricing" },
                { item: "FAQs" },
                { item: "About" },
            ];
        } else headerData = articlePageData.headerItems;

        if (articlePageData.footerItems.length == 0) {
            footerData = [
                { item: "Home" },
                { item: "Features" },
                { item: "Pricing" },
                { item: "FAQs" },
                { item: "About" },
            ];
        } else footerData = articlePageData.footerItems;

        var r = document.querySelector(":root");
        r.style.setProperty(
            "--data-mainBackgroundColor",
            articlePageData.colors.mainBackgroundColor
        );
        r.style.setProperty(
            "--data-secondaryBackgroundColor",
            articlePageData.colors.secondaryBackgroundColor
        );
        r.style.setProperty(
            "--data-newsHeaderBackgroundColor",
            articlePageData.colors.newsHeaderBackgroundColor
        );
        r.style.setProperty(
            "--data-mainTextColor",
            articlePageData.colors.mainTextColor
        );
        r.style.setProperty(
            "--data-secondaryTextColor",
            articlePageData.colors.secondaryTextColor
        );
        return articlePageData;
    }

    let pageLoaded = () => {
        console.log("loaded");
        // showSlides(slideIndex);
        console.log(sessionStorage.getItem("loggedIn"));
    };

    function openHamburgerMenu() {
        document.getElementById("hamburgerMenu").style.transform =
            "translateX(0)";
    }

    function closeHamburgerMenu() {
        document.getElementById("hamburgerMenu").style.transform =
            "translateX(-100%)";
    }

    function getParameterByName(name, url = window.location.href) {
        name = name.replace(/[\[\]]/g, "\\$&");
        var regex = new RegExp("[?&]" + name + "(=([^&#]*)|&|#|$)"),
            results = regex.exec(url);
        if (!results) return null;
        if (!results[2]) return "";
        return decodeURIComponent(results[2].replace(/\+/g, " "));
    }

    console.log(articleId);
</script>

{#await getarticlePageData()}
    Loafing page :v
{:then}
    <header id="mainHeader">
        <nav>
            <div id="headerContent">
                <img id="headerIcon" src="favicon.png" alt="icon" />
                {#each headerData as headerItem}
                    <a href="/#/">{headerItem.item}</a>
                {/each}
            </div>
            <div id="loginBtns">
                {#if sessionStorage.getItem("loggedIn") != "true"}
                    <a href="/#/logInPage" id="loginBtn">Log In</a>
                    <a href="/#/registerPage" id="registerBtn">Register</a>
                {:else}
                    <button
                        id="logOutBtn"
                        on:click={() => {
                            sessionStorage.setItem("loggedIn", "");
                            sessionStorage.setItem(
                                "userType",
                                "unregistered user"
                            );
                            window.location.reload();
                        }}>Log Out</button
                    >
                    <a href="/#/editPage" id="editPageBtn">Edit Page</a>
                    <a href="/#/themesEditPage" id="editPageBtn">Edit Theme</a>
                {/if}
            </div>
        </nav>
    </header>
    <header id="smallHeader">
        <nav>
            <div id="hamburger">
                <button on:click={openHamburgerMenu}>
                    <img
                        src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b2/Hamburger_icon.svg/1024px-Hamburger_icon.svg.png"
                        alt="hamburger"
                        id="hamburgerIcon"
                    />
                </button>
            </div>
            <div>
                <img id="headerIcon" src="favicon.png" alt="icon" />
            </div>
        </nav>
        <div id="hamburgerMenu">
            <button id="closeHamburgerMenuButton" on:click={closeHamburgerMenu}
                >&#10006;</button
            >
            <h2>CMS</h2>
            <hr />
            {#each headerData as headerItem}
                <a href="/#/">
                    {headerItem.item}
                </a>
                <hr />
            {/each}
            <a href="/#/gallery">Gallery</a>
            <hr />
            {#if sessionStorage.getItem("loggedIn") != "true"}
                <p>
                    <a
                        href="/#/logInPage"
                        style="color: #0b0;"
                        on:click={() => {
                            clearInterval(slideInterval);
                        }}>Log In</a
                    >
                </p>
                <hr />
                <p>
                    <a
                        href="/#/registerPage"
                        style="color: #00f;"
                        on:click={() => {
                            clearInterval(slideInterval);
                        }}>Register</a
                    >
                </p>
                <hr />
            {:else}
                <p>
                    <button
                        style="color: #f00;"
                        on:click={() => {
                            sessionStorage.setItem("loggedIn", "");
                            sessionStorage.setItem(
                                "userType",
                                "unregistered user"
                            );
                            window.location.reload();
                        }}>Log Out</button
                    >
                </p>
                <hr />
                <p>
                    <a
                        href="/#/editPage"
                        style="color: rgb(72, 187, 207);"
                        on:click={() => {
                            clearInterval(slideInterval);
                        }}>Edit Page</a
                    >
                </p>
                <hr />
                <p>
                    <a
                        href="/#/themesEditPage"
                        style="color: rgb(72, 187, 207);"
                        on:click={() => {
                            clearInterval(slideInterval);
                        }}>Edit Theme</a
                    >
                </p>
                <hr />
            {/if}
        </div>
    </header>

    <main id="articleMain">
        <h3>{currentArticle.header}</h3>
        <hr />
        <h1>{currentArticle.title}</h1>
        <p style="margin-bottom: 50px;">{currentArticle.article}</p>
        <hr />
    </main>

    <footer use:pageLoaded>
        <div id="footerContent">
            {#each footerData as footerItem}
                <p>{footerItem.item}</p>
            {/each}
        </div>
        <hr style="width:100%;" />
        &copy; 2022 Company, Inc.
    </footer>
{/await}
