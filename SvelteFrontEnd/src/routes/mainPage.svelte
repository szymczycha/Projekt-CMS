<script>
    let sliderData = [
        {
            imageUrl:
                "https://thumbs.gfycat.com/MiniatureGiddyKusimanse-max-1mb.gif",
            title: "Monke",
            description: "eet bananan",
            interval: 2000,
        },
        {
            imageUrl: "https://c.tenor.com/TTfEcL3R8ToAAAAC/monkeys.gif",
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
    let newsData = [
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
            slides[i].style.display = "none";
        }
        for (i = 0; i < dots.length; i++) {
            dots[i].classList.remove("active");
        }
        slides[slideIndex - 1].style.display = "block";
        dots[slideIndex - 1].classList.add("active");
        //console.log(slideIndex);
        clearInterval(slideInterval);
        slideInterval = window.setInterval(() => {
            slideIndex++;
            showSlides(slideIndex);
        }, sliderData[slideIndex - 1].interval);
    }

    window.onload = () => {
        showSlides(slideIndex);
        document.getElementById("userType").innerText =
            "Hi " +
            (sessionStorage.getItem("userType") ?? "unregisterred user");
        console.log(sessionStorage.getItem("loggedIn"));
    };
</script>

<header>
    <nav>
        <div>Icon</div>
        <div id="userType" />
        <div>
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
                        sessionStorage.setItem("userType", "");
                        window.location.reload();
                    }}>Log Out</button
                >
            {/if}
        </div>
    </nav>
</header>

<main>
    <div class="slideshow-container">
        <!-- Full-width images with number and caption text -->

        {#each sliderData as slide, i}
            <div class="mySlides fade">
                <div class="numbertext">{i + 1} / {sliderData.length}</div>
                <img
                    src={slide.imageUrl}
                    style="width:100%; max-height: 350px;"
                    alt="slider"
                />
                <div class="sliderContent">
                    <div class="text">{slide.title}</div>
                    <div class="subtext">{slide.description}</div>
                    <div style="text-align:center">
                        {#each sliderData as slide, i}
                            <span
                                class="dot"
                                on:click={() => currentSlide(i + 1)}
                            />
                        {/each}
                    </div>
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
    </div>
    <br />

    <div id="news-container">
        {#each newsData as news}
            <div class="newsBox">
                <div class="newsHeader">{news.header}</div>
                <div class="newsContent">
                    <h4>{news.title}</h4>
                    <p>{news.content}</p>
                    <button>{news.buttonText}</button>
                </div>
            </div>
        {/each}
    </div>
</main>
