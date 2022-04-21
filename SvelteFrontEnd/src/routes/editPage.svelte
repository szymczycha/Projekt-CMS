<script>
    let page = "base";
    
    function SetPage(name) {
        if(page != "base"){
            document.getElementById("select"+page).classList.toggle("selectedPage");
        }
        page = name;
        if(page != "base"){
            document.getElementById("select"+name).classList.toggle("selectedPage");
        }
    }
    async function getMainPageData(){
        const res = await fetch("/getMainPageData");
        return await res.json();
    }
</script>

<nav id="editNav">
    <div class="flexCenter" on:click={() => SetPage("Users")} id="selectUsers">Users</div>
    <div class="flexCenter" on:click={() => SetPage("Nav")} id="selectNav">Nav</div>
    <div class="flexCenter" on:click={() => SetPage("Slider")} id="selectSlider">Slider</div>
    <div class="flexCenter" on:click={() => SetPage("News")} id="selectNews">News</div>
    <div class="flexCenter" on:click={() => SetPage("Cards")} id="selectCards">Cards</div>
    <div class="flexCenter" on:click={() => SetPage("Footer")} id="selectFooter">Footer</div>
    <div class="flexCenter" on:click={() => SetPage("base")} id="selectFooter">Dane</div>
</nav>

{#await getMainPageData()}
    Waiting for data...
{:then data} 
    <main class="flexCenter" id="editMain">
        {#if page == "base"}
        <pre>{JSON.stringify(data, null, 2)}</pre>
        {:else if page == "Users"}
            Users
        {:else if page == "Nav"}
            Nav
        {:else if page == "Slider"}
            Slider
        {:else if page == "News"}
            <button class="editPageButton">Add new news</button>
            <div id="newsEditForms">
                {#each data.news as newsItem}
                    <pre>
                        {JSON.stringify(newsItem, null, 2)}
                    </pre>
                {/each}
            </div>
        {:else if page == "Cards"}
            Cards
        {:else if page == "Footer"}
            Footer
        {:else}
            Something went wrong
        {/if}
    </main>
{/await}
