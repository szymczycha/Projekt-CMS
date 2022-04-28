<script>
    let addItem = false;
    let page = "base";
    let editPageData;
    function SetPage(name) {
        addItem = false;
        if (page != "base") {
            document
                .getElementById("select" + page)
                .classList.toggle("selectedPage");
        }
        page = name;
        if (page != "base") {
            document
                .getElementById("select" + name)
                .classList.toggle("selectedPage");
        }
    
    }

</script>

<nav id="editNav">
    <div class="flexCenter" on:click={() => SetPage("Users")} id="selectUsers">
        Users
    </div>
    <div class="flexCenter" on:click={() => SetPage("Nav")} id="selectNav">
        Nav
    </div>
    <div
        class="flexCenter"
        on:click={() => SetPage("Slider")}
        id="selectSlider"
    >
        Slider
    </div>
    <div class="flexCenter" on:click={() => SetPage("News")} id="selectNews">
        News
    </div>
    <div class="flexCenter" on:click={() => SetPage("Cards")} id="selectCards">
        Cards
    </div>
    <div
        class="flexCenter"
        on:click={() => SetPage("Footer")}
        id="selectFooter"
    >
        Footer
    </div>
    <div class="flexCenter" on:click={() => SetPage("base")} id="selectFooter">
        RAW
    </div>
</nav>

