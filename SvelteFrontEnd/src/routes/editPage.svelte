<script>
    let page = "base";
    let editPageData;
    function SetPage(name) {
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
    async function getEditPageData() {
        const res = await fetch("/getEditPageData");
        editPageData = await res.json();
        return JSON.parse(JSON.stringify(editPageData));
    }

    async function saveData(i, data) {
        let dataToSend, key;
        switch (page) {
            case "Users":
                dataToSend = editPageData.users[i];
                key = data.users[i].username;
                break;
            case "Nav":
                dataToSend = editPageData.headerItems[i];
                key = data.headerItems[i].item;
                break;
            case "Slider":
                dataToSend = editPageData.sliderItems[i];
                key = data.sliderItems[i].title;
                break;
            case "News":
                dataToSend = editPageData.news[i];
                key = data.news[i].title;
                break;
            case "Cards":
                dataToSend = editPageData.contentCards[i];
                key = data.contentCards[i].title;
                break;
            case "Footer":
                dataToSend = editPageData.footerItems[i];
                key = data.footerItems[i].item;
                break;
            default:
                return "Wrong page id";
        }
        const res = await fetch("/editData", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                dataType: page,
                data: dataToSend,
                key: key,
            }),
        }).then((res) => console.log(res));
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

{#await getEditPageData()}
    Waiting for data...
{:then data}
    <main class="flexCenter" id="editMain">
        {#if page == "base"}
            <pre>{JSON.stringify(data, null, 2)}</pre>
        {:else if page == "Users"}
            <button class="editPageButton">Add new user</button>
            <div id="userEditForms" class="editForms">
                {#each editPageData.users as user, i}
                    <div class="flexCenter flexDirCol editPageForm">
                        <div class="flexSpaceBetween">
                            Username:
                            <input type="text" bind:value={user.username} />
                        </div>
                        <div class="flexSpaceBetween">
                            Password:
                            <input type="password" bind:value={user.password} />
                        </div>
                        <div class="flexSpaceBetween">
                            UserType:
                            <select bind:value={user.userType}>
                                <option value="admin">Administrator</option>
                                <option value="moderator">Moderator</option>
                                <option value="user">Basic user</option>
                            </select>
                        </div>
                        <button
                            class="editPageSaveButton"
                            on:click={() => saveData(i, data)}>Save</button
                        >
                    </div>
                {/each}
            </div>
        {:else if page == "Nav"}
            <button class="editPageButton">Add new user</button>
            <div id="headerEditForms" class="editForms">
                {#each editPageData.headerItems as headerItem, i}
                    <div class="flexCenter flexDirCol editPageForm">
                        <div class="flexSpaceBetween">
                            Item:
                            <input type="text" bind:value={headerItem.item} />
                        </div>
                        <button
                            class="editPageSaveButton"
                            on:click={() => saveData(i, data)}>Save</button
                        >
                    </div>
                {/each}
            </div>
        {:else if page == "Slider"}
            <button class="editPageButton">Add new SliderItem</button>
            <div id="sliderEditForms" class="editForms">
                {#each editPageData.sliderItems as sliderItem, i}
                    <div class="flexCenter flexDirCol editPageForm">
                        <div class="flexSpaceBetween">
                            Title:
                            <input type="text" bind:value={sliderItem.title} />
                        </div>
                        <div class="flexSpaceBetween">
                            Image URL:
                            <input
                                type="text"
                                bind:value={sliderItem.imageUrl}
                            />
                        </div>
                        <div class="flexSpaceBetween">
                            Description:
                            <input bind:value={sliderItem.description} />
                        </div>
                        <div class="flexSpaceBetween">
                            Interval:
                            <input
                                type="number"
                                min="0"
                                max="100000"
                                bind:value={sliderItem.interval}
                            />
                        </div>
                        <button
                            class="editPageSaveButton"
                            on:click={() => saveData(i, data)}>Save</button
                        >
                    </div>
                {/each}
            </div>
        {:else if page == "News"}
            <button class="editPageButton">Add new news</button>
            <div id="newsEditForms" class="editForms">
                {#each editPageData.news as newsItem, i}
                    <div class="flexCenter flexDirCol editPageForm">
                        <div class="flexSpaceBetween">
                            Title:
                            <input type="text" bind:value={newsItem.title} />
                        </div>
                        <div class="flexSpaceBetween">
                            Header:
                            <input type="text" bind:value={newsItem.header} />
                        </div>
                        <div class="flexSpaceBetween">
                            Content:
                            <textarea bind:value={newsItem.content} />
                        </div>
                        <div class="flexSpaceBetween">
                            Button text:
                            <input
                                type="text"
                                bind:value={newsItem.buttonText}
                            />
                        </div>
                        <button
                            class="editPageSaveButton"
                            on:click={() => saveData(i, data)}>Save</button
                        >
                    </div>
                {/each}
            </div>
        {:else if page == "Cards"}
            <button class="editPageButton">Add new card</button>
            <div id="cardsEditForms" class="editForms">
                {#each editPageData.contentCards as contentCard, i}
                    <div class="flexCenter flexDirCol editPageForm">
                        <div class="flexSpaceBetween">
                            Title:
                            <input type="text" bind:value={contentCard.title} />
                        </div>
                        <div class="flexSpaceBetween">
                            Subtitle:
                            <input
                                type="text"
                                bind:value={contentCard.subtitle}
                            />
                        </div>
                        <div class="flexSpaceBetween">
                            Image Url:
                            <input
                                type="text"
                                bind:value={contentCard.imageURL}
                            />
                        </div>
                        <div class="flexSpaceBetween">
                            Content:
                            <textarea bind:value={contentCard.content} />
                        </div>
                        <div class="flexSpaceBetween">
                            Is On Left Side:
                            <input
                                type="checkbox"
                                bind:checked={contentCard.isImageOnLeftSide}
                            />
                        </div>

                        <button
                            class="editPageSaveButton"
                            on:click={() => saveData(i, data)}>Save</button
                        >
                    </div>
                {/each}
            </div>
        {:else if page == "Footer"}
            <button class="editPageButton">Add new footerItem</button>
            <div id="footerEditForms" class="editForms">
                {#each editPageData.footerItems as footerItem, i}
                    <div class="flexCenter flexDirCol editPageForm">
                        <div class="flexSpaceBetween">
                            Item:
                            <input type="text" bind:value={footerItem.item} />
                        </div>
                        <button
                            class="editPageSaveButton"
                            on:click={() => saveData(i, data)}>Save</button
                        >
                    </div>
                {/each}
            </div>
        {:else}
            Something went wrong
        {/if}
    </main>
{/await}
