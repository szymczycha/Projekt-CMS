<script>
    let mainPageData;
    let sliderData;
    let newsData;
    let contentCardsData;
    let headerData;
    let footerData;
    async function getMainPageData() {
        const res = await fetch("/getMainPageData");
        mainPageData = await res.json();
        console.log(mainPageData);

        if (mainPageData.sliderItems.length == 0) {
            console.log("h");
            sliderData = [
                {
                    imageUrl:
                        "https://thumbs.gfycat.com/MiniatureGiddyKusimanse-max-1mb.gif",
                    title: "Monke",
                    description: "eet bananan",
                    interval: 2000,
                },
                {
                    imageUrl:
                        "https://c.tenor.com/TTfEcL3R8ToAAAAC/monkeys.gif",
                    title: "Monke2",
                    description: "where bananan",
                    interval: 5000,
                },
                {
                    imageUrl:
                        "https://media.discordapp.net/attachments/683372664546525228/911289580148367400/gomus.gif",
                    title: "gomus))",
                    description: "my beloverd",
                    interval: 10000,
                },
            ];
        } else sliderData = mainPageData.sliderItems;

        if (mainPageData.news.length == 0) {
            newsData = [
                {
                    header: "News 1",
                    title: "Holy hsit guise",
                    content: "lorem ipus",
                    buttonText: "going",
                },
                {
                    header: "News dwa",
                    title: "Sample tect",
                    content: "lorm imbus",
                    buttonText: "button.text",
                },
                {
                    header: "News 3",
                    title: "))))))))",
                    content: "l'oreal igloo",
                    buttonText: "[Object[Object]]",
                },
            ];
        } else newsData = mainPageData.news;

        if (mainPageData.contentCards.length == 0) {
            contentCardsData = [
                {
                    title: "Page content 1",
                    subtitle: "This is sub tile",
                    content:
                        "is going to b epic card yeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee",
                    imageURL:
                        "https://media.discordapp.net/attachments/640672443710701568/901173807841153084/image0-1.png?width=633&height=676",
                    isImageOnLeftSide: false,
                },
                {
                    title: "Page contet 2",
                    subtitle: "This sub is titl",
                    content:
                        "<scripr> while(true) program.hack(you); print(':)');<scirp/>",
                    imageURL:
                        "https://media.discordapp.net/attachments/741945274901200897/885139560135295006/image0-105.gif",
                    isImageOnLeftSide: true,
                },
                {
                    title: "Page content e",
                    subtitle: "Telk is soup",
                    content:
                        "mik uderzył psa to mu powiedziałem co ty robisz nie bij psa a on mi mów nie udzerzyłem patrz to jest uderzenie i mnie uderzył w kolano to ja go uderzyłem w czaszke z pięsci i mamie się to niespodobało ",
                    imageURL:
                        "https://media.discordapp.net/attachments/659630509894271001/793958618377748492/image0-37.gif",
                    isImageOnLeftSide: false,
                },
            ];
        } else contentCardsData = mainPageData.contentCards;

        if (mainPageData.headerItems.length == 0) {
            headerData = [
                { item: "Features" },
                { item: "Pricing" },
                { item: "FAQs" },
                { item: "About" },
            ];
        } else headerData = mainPageData.headerItems;

        if (mainPageData.footerItems.length == 0) {
            footerData = [
                { item: "Features" },
                { item: "Pricing" },
                { item: "FAQs" },
                { item: "About" },
            ];
        } else footerData = mainPageData.footerItems;

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
            showSlides(slideIndex);
        }, sliderData[slideIndex - 1].interval);
    }

    let pageLoaded = () => {
        console.log("loaded");
        showSlides(slideIndex);
        console.log(sessionStorage.getItem("loggedIn"));
    };

    window.onresize = () => {
        console.log(
            document.getElementsByClassName("slideshow-container")[0].style
        );
        document.getElementsByClassName(
            "slideshow-container"
        )[0].style.height = `${
            window.innerWidth /
            (2.84 * Math.sin((((window.innerWidth - 320) / 1920) * 3.14) / 2) +
                1)
        }px`;
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
                            sessionStorage.setItem("username", "");
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

    <main>
        <div class="slideshow-container">
            <!-- Full-width images with number and caption text -->

            {#each sliderData as slide, i}
                <div class="mySlides fade">
                    <div class="numbertext">{i + 1} / {sliderData.length}</div>
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
                    <span class="dot" on:click={() => currentSlide(i + 1)} />
                {/each}
            </div>
        </div>
        <br />

        <div id="news-container">
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
        </div>

        <div id="contentCards-container">
            {#each contentCardsData as card}
                <hr />
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
                        <p>{card.content}</p>
                    </div>
                    <img
                        class="cardImg"
                        src={card.imageURL}
                        alt={card.imageURL}
                    />
                </div>
            {/each}
            <hr />
        </div>
    </main>

    <footer use:pageLoaded>
        <div id="footerContent">
            <a href="/#/">Home</a>
            {#each footerData as footerItem}
                <a href="/#/">{footerItem.item}</a>
            {/each}
            <a href="/#/gallery">Gallery</a>
        </div>
        <hr style="width:100%;" />
        &copy; 2022 Company, Inc.
    </footer>
    <div use:resizeSlider />
{/await}
