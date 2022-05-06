<script>
    let addItem = false;
    let page = "base";
    let themesData;
    let selectedThemeId;
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
        return JSON.parse(JSON.stringify(themesData));
    }
    async function addTheme(){
        console.log({
                name: document.getElementById("name").value,
                mainBackgroundColor: document.getElementById("mainBackgroundColor").value,
                secondaryBackgroundColor: document.getElementById("secondaryBackgroundColor").value,
                newsHeaderBackgroundColor: document.getElementById("newsHeaderBackgroundColor").value,
                mainTextColor: document.getElementById("mainTextColor").value,
                secondaryTextColor: document.getElementById("secondaryTextColor").value,
            });
        await fetch("/addTheme", 
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                name: document.getElementById("name").value,
                mainBackgroundColor: document.getElementById("mainBackgroundColor").value,
                secondaryBackgroundColor: document.getElementById("secondaryBackgroundColor").value,
                newsHeaderBackgroundColor: document.getElementById("newsHeaderBackgroundColor").value,
                mainTextColor: document.getElementById("mainTextColor").value,
                secondaryTextColor: document.getElementById("secondaryTextColor").value,
            }),
        })
        .then(res => res.json())
        .then((res) => {
            console.log(res);
            if(res.showError){
                errorMessageVisible = true;
                errorMessage = `There was a problem while adding this theme: ${res.result}`
            }
        });
    }
    function onSelectTheme(){
        let selectedTheme;
        themesData.themes.forEach(theme => {
            if(theme.id == selectedThemeId){
                selectedTheme = JSON.parse(JSON.stringify(theme));
            }
        });
        document.getElementById("mainBackgroundColor").value = selectedTheme.mainBackgroundColor;
        document.getElementById("secondaryBackgroundColor").value = selectedTheme.secondaryBackgroundColor;
        document.getElementById("newsHeaderBackgroundColor").value = selectedTheme.newsHeaderBackgroundColor;
        document.getElementById("mainTextColor").value = selectedTheme.mainTextColor;
        document.getElementById("secondaryTextColor").value = selectedTheme.secondaryTextColor;
    }
    async function selectTheme(){
        await fetch("/selectTheme", 
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                selectedThemeId: selectedThemeId,
                mainBackgroundColor: document.getElementById("mainBackgroundColor").value,
                secondaryBackgroundColor: document.getElementById("secondaryBackgroundColor").value,
                newsHeaderBackgroundColor: document.getElementById("newsHeaderBackgroundColor").value,
                mainTextColor: document.getElementById("mainTextColor").value,
                secondaryTextColor: document.getElementById("secondaryTextColor").value,
            }),
        })
        .then(res => res.json())
        .then((res) => {
            console.log(res);
        });
    }
</script>

<nav id="editNav">
    <div class="flexCenter" on:click={() => SetPage("Theme")} id="selectTheme">
        Select theme
    </div>
    <div class="flexCenter" on:click={() => SetPage("AddTheme")} id="selectAddTheme">
        AddTheme
    </div>
    <div class="flexCenter" on:click={() => SetPage("base")} id="selectFooter">
        RAW
    </div>
</nav>

{#await getThemes()}
    Loafing themes ^w^
{:then data}
    <main class="flexCenter" id="editMain">
        {#if page == "base"}
            <pre>{JSON.stringify(themesData, null, 2)}</pre>
        {:else if page == "Theme"}
        <div class="editPageForm">
            <select bind:value="{selectedThemeId}" on:change="{onSelectTheme}">
                {#each data.themes as theme,i}
                    <option value="{theme.id}">{theme.name}</option>
                {/each}
            </select>
            <div class="flexSpaceBetween">
                Main Background Color: 
                <input type="color" id="mainBackgroundColor" value="{themesData.themes[0].mainBackgroundColor}">
            </div>
            <div class="flexSpaceBetween">
                Secondary Background Color: 
                <input type="color" id="secondaryBackgroundColor" value="{themesData.themes[0].secondaryBackgroundColor}">
            </div>
            <div class="flexSpaceBetween">
                News Header Background Color: 
                <input type="color" id="newsHeaderBackgroundColor" value="{themesData.themes[0].newsHeaderBackgroundColor}">
            </div>
            <div class="flexSpaceBetween">
                Main Text Color: 
                <input type="color" id="mainTextColor" value="{themesData.themes[0].mainTextColor}">
            </div>
            <div class="flexSpaceBetween">
                Secondary Text Color: 
                <input type="color" id="secondaryTextColor" value="{themesData.themes[0].secondaryTextColor}">
            </div>
            <input type="hidden" value="">
            <button class="editPageSaveButton" on:click="{selectTheme}">Select</button>
        </div>
        {:else if page == "AddTheme"}
        <div class="editPageForm">
            
            <div class="flexSpaceBetween">
                Theme name: 
                <input type="text" id="name">
            </div>
            <div class="flexSpaceBetween">
                Main Background Color: 
                <input type="color" id="mainBackgroundColor">
            </div>
            <div class="flexSpaceBetween">
                Secondary Background Color: 
                <input type="color" id="secondaryBackgroundColor">
            </div>
            <div class="flexSpaceBetween">
                News Header Background Color: 
                <input type="color" id="newsHeaderBackgroundColor">
            </div>
            <div class="flexSpaceBetween">
                Main Text Color: 
                <input type="color" id="mainTextColor">
            </div>
            <div class="flexSpaceBetween">
                Secondary Text Color: 
                <input type="color" id="secondaryTextColor">
            </div>
            <button class="editPageSaveButton" on:click="{addTheme}">Add</button>
        </div>
        {:else}
            Something went wrong
        {/if}
    </main>
{/await}
