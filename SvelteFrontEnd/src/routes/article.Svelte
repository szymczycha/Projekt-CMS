<script>
    let articleId = getParameterByName("id");
    let articlePageData;
    let commentData;
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

        await getComments();

        return articlePageData;
    }

    async function getComments() {
        const res = await fetch("/getComments", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                articleId: articleId,
            }),
        })
            .then((res) => res.json())
            .then((res) => {
                commentData = res.comments;
                console.log(commentData);
            });
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

    async function addComment() {
        await fetch("/addComment", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                articleId: articleId,
                author: sessionStorage.username,
                date: Date(Date.now()).split(" ").slice(1, 5).join(" "),
                content: document.getElementById("commentContent").value,
            }),
        })
            .then((res) => res.json())
            .then((res) => {
                console.log(res);
                document.getElementById("commentContent").value = "";
                getComments();
            });
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
                <a href="/#/">Home</a>
                {#each headerData as headerItem}
                    <a href="/#/">{headerItem.item}</a>
                {/each}
                <a href="/#/gallery">Gallery</a>
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
                    <span class="material-symbols-outlined"> menu </span>
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
        <hr style="width: 100%;" />
        <h1>{currentArticle.title}</h1>
        <p style="white-space: pre-wrap;">{currentArticle.article}</p>

        <hr style="margin-top: 50px; width: 100%;" />

        <div id="bigCommentsContainer">
            <div id="comments">
                <h4>Comments:</h4>
                {#if commentData.length == 0}
                    <p style="opacity: 0.8;">No comments yet...</p>
                {:else}
                    <div class="commentsContainer">
                        {#each commentData as comment}
                            <div class="comment">
                                <div class="commentHeader">
                                    <img
                                        src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/98/OOjs_UI_icon_userAvatar.svg/1200px-OOjs_UI_icon_userAvatar.svg.png"
                                        alt="user"
                                        class="userIcon"
                                    />
                                    <p>{comment.author}</p>
                                </div>

                                <p class="commentContent">
                                    {comment.content}
                                </p>

                                <div class="commentFooter">
                                    <p class="commentDate">{comment.date}</p>
                                </div>
                            </div>
                        {/each}
                    </div>
                {/if}
                <hr />
                {#if sessionStorage.loggedIn == "true"}
                    <h4>Write a comment:</h4>
                    <div id="newComment">
                        <textarea id="commentContent" />
                        <br />
                        <button on:click={addComment}>Send</button>
                    </div>
                {:else}
                    <h4>Log in to add a comment!</h4>
                {/if}
            </div>
        </div>

        <hr style="margin-top: 50px; width: 100%;" />
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
