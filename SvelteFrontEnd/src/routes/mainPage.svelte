<script>
    
    let sliderData = [
        {imageUrl: "https://thumbs.gfycat.com/MiniatureGiddyKusimanse-max-1mb.gif", title: "Monke", description: "eet bananan"},
        {imageUrl: "https://thumbs.gfycat.com/MiniatureGiddyKusimanse-max-1mb.gif", title: "Monke2", description: "eet bananan"},
        {imageUrl: "https://thumbs.gfycat.com/MiniatureGiddyKusimanse-max-1mb.gif", title: "Monke3", description: "eet bananan"}
    ]

    let slideIndex = 1;

    // Next/previous controls
    function plusSlides(n) {
        showSlides(slideIndex += n);
    }

    // Thumbnail image controls
    function currentSlide(n) {
        showSlides(slideIndex = n);
    }

    function showSlides(n) {
        let i;
        let slides = document.getElementsByClassName("mySlides");
        //console.log(slides)
        let dots = document.getElementsByClassName("dot");
        if (n > slides.length) {slideIndex = 1}
        if (n < 1) {slideIndex = slides.length}
        for (i = 0; i < slides.length; i++) {
            slides[i].style.display = "none";
        }
        for (i = 0; i < dots.length; i++) {
            dots[i].classList.remove("active");
        }
        slides[slideIndex-1].style.display = "block";
        dots[slideIndex-1].classList.add("active");
    }

    window.onload = () => {
        showSlides(slideIndex)
    }
</script>

<header>
    <nav>
        <div>
            Icon
        </div>
        <div>
            <a href="/#/logInPage" id="loginBtn">Log In</a>
            <a href="/#/registerPage" id="registerBtn">Register</a>
        </div>
    </nav>
</header>

<main>
    <div class="slideshow-container">

    <!-- Full-width images with number and caption text -->
        
    {#each sliderData as slide, i}
    <div class="mySlides fade">
        <div class="numbertext">{i+1} / {sliderData.length}</div>
        <img src="{slide.imageUrl}" style="width:100%; max-height: 300px;" alt="slider"/>
        <div class="text">{slide.title}</div>
        <div class="subtext">{slide.description}</div>
    </div>
    {/each}

    <!-- Next and previous buttons -->
    <button id="prev" class="prev" on:click={() => plusSlides(-1)}>&#10094;</button>
    <button id="next" class="next" on:click={() => plusSlides(1)}>&#10095;</button>
    </div>
    <br>

    <!-- The dots/circles -->
    <div style="text-align:center">
        {#each sliderData as slide, i}
            <span class="dot" on:click={() => currentSlide(i+1)}></span>
        {/each}
    </div>
</main>