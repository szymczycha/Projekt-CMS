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
        
    {#each sliderData as slide}
    <div class="mySlides fade">
        <div class="numbertext">1 / 3</div>
        <img src="{slide.imageUrl}" style="width:100%" alt="slider"/>
        <div class="text">{slide.title}</div>
    </div>
    {/each}

    <!-- Next and previous buttons -->
    <a class="prev" onclick="plusSlides(-1)">&#10094;</a>
    <a class="next" onclick="plusSlides(1)">&#10095;</a>
    </div>
    <br>

    <!-- The dots/circles -->
    <div style="text-align:center">
        {#each sliderData as slide, i}
            <span class="dot" onclick="currentSlide({i})"></span>
        {/each}
    </div>
    {showSlides(slideIndex)}
</main>

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
        console.log(slides)
        let dots = document.getElementsByClassName("dot");
        if (n > slides.length) {slideIndex = 1}
        if (n < 1) {slideIndex = slides.length}
        for (i = 0; i < slides.length; i++) {
            slides[i].style.display = "none";
        }
        for (i = 0; i < dots.length; i++) {
            dots[i].className = dots[i].className.replace(" active", "");
        }
        slides[slideIndex-1].style.display = "block";
        dots[slideIndex-1].className += "active";
    }
</script>