<script>
    let addItem = false;
    let page = "base";
    let themesData;
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
    async function getThemes(){
        const res = await fetch("/getThemes");
        themesData = await res.json();
        console.log(themesData);
    }

</script>

<nav id="editNav">
    <div class="flexCenter" on:click={() => SetPage("Users")} id="selectTheme">
        Select theme
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

{#await getThemes()}
    Loafing themes ^w^
{:then}
    <main class="flexCenter" id="editMain">
        {#if page == "base"}
            <pre>{JSON.stringify(themesData, null, 2)}</pre>
        {:else if page == "Users"}
            <input type="color">
        {:else if page == "Nav"}
            NAV
        {:else if page == "Slider"}
            SLIDER
        {:else if page == "News"}
            News
        {:else if page == "Cards"}
            CARDS
        {:else if page == "Footer"}
            FOOTER
        {:else}
            Something went wrong
        {/if}
    </main>
{/await}
