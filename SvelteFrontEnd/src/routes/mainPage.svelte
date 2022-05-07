<script>
    let mainPageData;
    let sliderData;
    let newsData;
    let contentCardsData;
    let headerData;
    let footerData;
    let layout;
    let sliderVisible = true;
    async function getMainPageData() {
        const res = await fetch("/getMainPageData");
        mainPageData = await res.json();
        console.log(mainPageData);

        sliderData = mainPageData.sliderItems;
        if (sliderData.length <= 0) sliderVisible = false;

        newsData = mainPageData.news;

        contentCardsData = mainPageData.contentCards;

        headerData = mainPageData.headerItems;

        footerData = mainPageData.footerItems;

        var r = document.querySelector(":root");
        r.style.setProperty(
            "--data-mainBackgroundColor",
            mainPageData.colors.mainBackgroundColor
        );
        r.style.setProperty(
            "--data-secondaryBackgroundColor",
            mainPageData.colors.secondaryBackgroundColor
        );
        r.style.setProperty(
            "--data-newsHeaderBackgroundColor",
            mainPageData.colors.newsHeaderBackgroundColor
        );
        r.style.setProperty(
            "--data-mainTextColor",
            mainPageData.colors.mainTextColor
        );
        r.style.setProperty(
            "--data-secondaryTextColor",
            mainPageData.colors.secondaryTextColor
        );

        layout = mainPageData.layout.split(",");
    }

    let slideIndex = 1;
    let slideInterval;

    // Next/previous controls
    function plusSlides(n) {
        clearInterval(slideInterval);
        showSlides((slideIndex += n));
    }

    // Thumbnail image controls
    function currentSlide(n) {
        clearInterval(slideInterval);
        showSlides((slideIndex = n));
    }

    function showSlides(n) {
        let i;
        let slides = document.getElementsByClassName("mySlides");
        //console.log(slides)
        let dots = document.getElementsByClassName("dot");
        if (n > slides.length) {
            slideIndex = 1;
        }
        if (n < 1) {
            slideIndex = slides.length;
        }
        for (i = 0; i < slides.length; i++) {
            //slides[i].style.display = "none";
            slides[i].classList.remove("visibleSlide");
            slides[i].classList.add("fade");
        }
        for (i = 0; i < dots.length; i++) {
            dots[i].classList.remove("active");
        }
        //slides[slideIndex - 1].style.display = "block";
        slides[slideIndex - 1].classList.add("visibleSlide");
        slides[slideIndex - 1].classList.remove("fade");
        dots[slideIndex - 1].classList.add("active");
        //console.log(slideIndex);
        clearInterval(slideInterval);
        slideInterval = window.setInterval(() => {
            slideIndex++;
            try {
                showSlides(slideIndex);
            } catch {
                console.log("Interval stopped");
                clearInterval(slideInterval);
            }
        }, sliderData[slideIndex - 1].interval);
    }

    let pageLoaded = () => {
        console.log("loaded");
        if (sliderVisible) showSlides(slideIndex);
        console.log(sessionStorage.getItem("loggedIn"));
    };

    window.onresize = () => {
        try {
            document.getElementsByClassName(
                "slideshow-container"
            )[0].style.height = `${
                window.innerWidth /
                (2.84 *
                    Math.sin((((window.innerWidth - 320) / 1920) * 3.14) / 2) +
                    1)
            }px`;
        } catch {
            // console.log("h");
            window.onresize = null;
        }
    };
    function resizeSlider() {
        document.getElementsByClassName(
            "slideshow-container"
        )[0].style.height = `${
            window.innerWidth /
            (2.84 * Math.sin((((window.innerWidth - 320) / 1920) * 3.14) / 2) +
                1)
        }px`;
    }

    function openHamburgerMenu() {
        document.getElementById("hamburgerMenu").style.transform =
            "translateX(0)";
    }

    function closeHamburgerMenu() {
        document.getElementById("hamburgerMenu").style.transform =
            "translateX(-100%)";
    }
</script>

{#await getMainPageData()}
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
                    <a
                        href="/#/logInPage"
                        id="loginBtn"
                        on:click={() => {
                            clearInterval(slideInterval);
                        }}>Log In</a
                    >
                    <a
                        href="/#/registerPage"
                        id="registerBtn"
                        on:click={() => {
                            clearInterval(slideInterval);
                        }}>Register</a
                    >
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
                    {#if sessionStorage.userType == "moderator" || sessionStorage.userType == "admin"}
                        <a
                            href="/#/editPage"
                            id="editPageBtn"
                            on:click={() => {
                                clearInterval(slideInterval);
                            }}>Edit Page</a
                        >
                        <a
                            href="/#/themesEditPage"
                            id="editPageBtn"
                            on:click={() => {
                                clearInterval(slideInterval);
                            }}>Edit Theme</a
                        >
                    {/if}
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
            <a href="/#/">Home</a>
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
                            sessionStorage.setItem("username", "");
                            window.location.reload();
                        }}>Log Out</button
                    >
                </p>
                <hr />
                {#if sessionStorage.userType == "moderator" || sessionStorage.userType == "admin"}
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
            {/if}
        </div>
    </header>

    <main>
        {#if sliderVisible}
            <div
                class="slideshow-container"
                style={`order: ${layout.indexOf("slider")};`}
            >
                <!-- Full-width images with number and caption text -->

                {#each sliderData as slide, i}
                    <div class="mySlides fade">
                        <div class="numbertext">
                            {i + 1} / {sliderData.length}
                        </div>
                        <img src={slide.imageUrl} alt="slider" />
                        <div class="sliderContent">
                            <div class="text">{slide.title}</div>
                            <div class="subtext">{slide.description}</div>
                        </div>
                    </div>
                {/each}

                <!-- Next and previous buttons -->
                <button id="prev" class="prev" on:click={() => plusSlides(-1)}
                    >&#10094;</button
                >
                <button id="next" class="next" on:click={() => plusSlides(1)}
                    >&#10095;</button
                >
                <div style="text-align:center" id="dotsContainer">
                    {#each sliderData as slide, i}
                        <span
                            class="dot"
                            on:click={() => currentSlide(i + 1)}
                        />
                    {/each}
                </div>
            </div>
            <br />
        {/if}

        <div id="news-container" style={`order: ${layout.indexOf("news")};`}>
            {#each newsData as news}
                <div class="newsBox">
                    <div class="newsHeader">{news.header}</div>
                    <div class="newsContent">
                        <h4>{news.title}</h4>
                        <p>{news.content}</p>
                        <a
                            href={`/#/article?id=${news.id}`}
                            on:click={clearInterval(slideInterval)}
                            ><button>{news.buttonText}</button></a
                        >
                    </div>
                </div>
            {/each}
            <hr style="width: 100%;" />
        </div>

        <div
            id="contentCards-container"
            style={`order: ${layout.indexOf("contentCards")};`}
        >
            {#each contentCardsData as card}
                <div
                    class="card"
                    style="flex-direction:{card.isImageOnLeftSide
                        ? 'row-reverse'
                        : 'row'};"
                >
                    <div
                        class="cardContent"
                        style="text-align:{card.isImageOnLeftSide
                            ? 'right'
                            : 'left'};"
                    >
                        <h4>{card.title}</h4>
                        <h5>{card.subtitle}</h5>
                        <p style="white-space: pre-wrap;">{card.content}</p>
                    </div>
                    <img
                        class="cardImg"
                        src={card.imageURL}
                        alt={card.imageURL}
                    />
                </div>
                <hr />
            {/each}
        </div>
    </main>

    <footer use:pageLoaded>
        {#if layout[2] == "slider"}
            <hr style="width: 100%;" />
        {/if}
        <div id="footerContent">
            <a href="/#/">Home</a>
            {#each footerData as footerItem}
                <a href="/#/">{footerItem.item}</a>
            {/each}
            <a href="/#/gallery">Gallery</a>
        </div>
        <hr style="width:100%;" />
        &copy; 2022 | Szymon Konieczny | Antoni Leszczyński
    </footer>
    {#if sliderVisible}
        <div use:resizeSlider />
    {/if}
{/await}
