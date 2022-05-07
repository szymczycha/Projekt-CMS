<script>
    let addItem = false;
    let page = "base";
    let themesData;
    let selectedThemeId;
    let selectedTheme;
    let layout;
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
    async function getThemes() {
        const res = await fetch("/getThemes");
        themesData = await res.json();
        console.log(themesData);
        selectedThemeId = themesData.selectedThemeId;
        themesData.themes.forEach((theme) => {
            if (theme.id == selectedThemeId) {
                selectedTheme = JSON.parse(JSON.stringify(theme));
            }
        });
        console.log(selectedThemeId);
        layout = themesData.layout.split(",");
        return JSON.parse(JSON.stringify(themesData));
    }
    async function addTheme() {
        console.log({
            name: document.getElementById("name").value,
            mainBackgroundColor: document.getElementById("mainBackgroundColor")
                .value,
            secondaryBackgroundColor: document.getElementById(
                "secondaryBackgroundColor"
            ).value,
            newsHeaderBackgroundColor: document.getElementById(
                "newsHeaderBackgroundColor"
            ).value,
            mainTextColor: document.getElementById("mainTextColor").value,
            secondaryTextColor:
                document.getElementById("secondaryTextColor").value,
        });
        await fetch("/addTheme", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                name: document.getElementById("name").value,
                mainBackgroundColor: document.getElementById(
                    "mainBackgroundColor"
                ).value,
                secondaryBackgroundColor: document.getElementById(
                    "secondaryBackgroundColor"
                ).value,
                newsHeaderBackgroundColor: document.getElementById(
                    "newsHeaderBackgroundColor"
                ).value,
                mainTextColor: document.getElementById("mainTextColor").value,
                secondaryTextColor:
                    document.getElementById("secondaryTextColor").value,
            }),
        })
            .then((res) => res.json())
            .then((res) => {
                console.log(res);
                window.location.reload();
            });
    }
    function onSelectTheme() {
        selectedThemeId = document.getElementById("themeNameSelect").value;
        themesData.themes.forEach((theme) => {
            if (theme.id == selectedThemeId) {
                selectedTheme = JSON.parse(JSON.stringify(theme));
            }
        });
        document.getElementById("mainBackgroundColor").value =
            selectedTheme.mainBackgroundColor;
        document.getElementById("secondaryBackgroundColor").value =
            selectedTheme.secondaryBackgroundColor;
        document.getElementById("newsHeaderBackgroundColor").value =
            selectedTheme.newsHeaderBackgroundColor;
        document.getElementById("mainTextColor").value =
            selectedTheme.mainTextColor;
        document.getElementById("secondaryTextColor").value =
            selectedTheme.secondaryTextColor;
    }
    async function selectTheme() {
        await fetch("/selectTheme", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                selectedThemeId: selectedThemeId,
                mainBackgroundColor: document.getElementById(
                    "mainBackgroundColor"
                ).value,
                secondaryBackgroundColor: document.getElementById(
                    "secondaryBackgroundColor"
                ).value,
                newsHeaderBackgroundColor: document.getElementById(
                    "newsHeaderBackgroundColor"
                ).value,
                mainTextColor: document.getElementById("mainTextColor").value,
                secondaryTextColor:
                    document.getElementById("secondaryTextColor").value,
            }),
        })
            .then((res) => res.json())
            .then((res) => {
                console.log(res);
            });
    }
    var r = document.querySelector(":root");
    r.style.setProperty("--data-mainBackgroundColor", "#333");
    r.style.setProperty("--data-secondaryBackgroundColor", "#ddd");
    r.style.setProperty("--data-newsHeaderBackgroundColor", "#999");
    r.style.setProperty("--data-mainTextColor", "#ddd");
    r.style.setProperty("--data-secondaryTextColor", "#000");

    function layoutSwap(i, j) {
        let tmp = layout[j];
        layout[j] = layout[i];
        layout[i] = tmp;
    }

    async function saveLayout() {
        await fetch("/saveLayout", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                layout: layout.join(","),
            }),
        })
            .then((res) => res.json())
            .then((res) => {
                console.log(res);
            });
    }
</script>

<nav id="editNav">
    {#if sessionStorage.userType == "moderator" || sessionStorage.userType == "admin"}
        <div
            class="flexCenter"
            on:click={() => SetPage("Theme")}
            id="selectTheme"
        >
            Select theme
        </div>
        <div
            class="flexCenter"
            on:click={() => SetPage("AddTheme")}
            id="selectAddTheme"
        >
            Add Theme
        </div>
        <div
            class="flexCenter"
            on:click={() => SetPage("PageLayout")}
            id="selectPageLayout"
        >
            Page Layout
        </div>
        <div
            class="flexCenter"
            on:click={() => SetPage("base")}
            id="selectFooter"
        >
            Raw data
        </div>
    {:else}
        Only moderators or admins can edit the themes
    {/if}
    <a href="/#/" class="flexCenter">Back</a>
</nav>

{#await getThemes()}
    Loafing themes ^w^
{:then data}
    <main class="flexCenter" id="editMain">
        {#if page == "base"}
            <pre>{JSON.stringify(themesData, null, 2)}</pre>
        {:else if page == "Theme"}
            <div class="editPageForm">
                <select on:change={onSelectTheme} id="themeNameSelect">
                    {#each data.themes as theme, i}
                        {console.log(theme.id.toString(), selectedThemeId)}
                        {#if theme.id.toString() == selectedThemeId}
                            <option value={theme.id} selected
                                >{theme.name}</option
                            >
                        {:else}
                            <option value={theme.id}>{theme.name}</option>
                        {/if}
                    {/each}
                </select>
                <div class="flexSpaceBetween">
                    Main Background Color:
                    <input
                        type="color"
                        id="mainBackgroundColor"
                        value={selectedTheme.mainBackgroundColor}
                    />
                </div>
                <div class="flexSpaceBetween">
                    Secondary Background Color:
                    <input
                        type="color"
                        id="secondaryBackgroundColor"
                        value={selectedTheme.secondaryBackgroundColor}
                    />
                </div>
                <div class="flexSpaceBetween">
                    News Header Background Color:
                    <input
                        type="color"
                        id="newsHeaderBackgroundColor"
                        value={selectedTheme.newsHeaderBackgroundColor}
                    />
                </div>
                <div class="flexSpaceBetween">
                    Main Text Color:
                    <input
                        type="color"
                        id="mainTextColor"
                        value={selectedTheme.mainTextColor}
                    />
                </div>
                <div class="flexSpaceBetween">
                    Secondary Text Color:
                    <input
                        type="color"
                        id="secondaryTextColor"
                        value={selectedTheme.secondaryTextColor}
                    />
                </div>
                <input type="hidden" value="" />
                <button class="editPageSaveButton" on:click={selectTheme}
                    >Select</button
                >
            </div>
        {:else if page == "AddTheme"}
            <div class="editPageForm">
                <div class="flexSpaceBetween">
                    Theme name:
                    <input type="text" id="name" />
                </div>
                <div class="flexSpaceBetween">
                    Main Background Color:
                    <input type="color" id="mainBackgroundColor" />
                </div>
                <div class="flexSpaceBetween">
                    Secondary Background Color:
                    <input type="color" id="secondaryBackgroundColor" />
                </div>
                <div class="flexSpaceBetween">
                    News Header Background Color:
                    <input type="color" id="newsHeaderBackgroundColor" />
                </div>
                <div class="flexSpaceBetween">
                    Main Text Color:
                    <input type="color" id="mainTextColor" />
                </div>
                <div class="flexSpaceBetween">
                    Secondary Text Color:
                    <input type="color" id="secondaryTextColor" />
                </div>
                <button class="editPageSaveButton" on:click={addTheme}
                    >Add</button
                >
            </div>
        {:else if page == "PageLayout"}
            <div class="editPageForm">
                {#each layout as layoutItem, i}
                    <div class="layoutItem">
                        {#if i == 0}
                            <button disabled>&#8593;</button>
                        {:else}
                            <button on:click={() => layoutSwap(i, i - 1)}
                                >&#8593;</button
                            >
                        {/if}
                        <p>{layoutItem}</p>
                        {#if i == 2}
                            <button disabled>&#8595;</button>
                        {:else}
                            <button on:click={() => layoutSwap(i, i + 1)}
                                >&#8595;</button
                            >
                        {/if}
                    </div>
                {/each}
                <div class="buttonCenterizer">
                    <button class="editPageSaveButton" on:click={saveLayout}
                        >Save Layout</button
                    >
                </div>
            </div>
        {:else}
            Something went wrong
        {/if}
    </main>
{/await}
