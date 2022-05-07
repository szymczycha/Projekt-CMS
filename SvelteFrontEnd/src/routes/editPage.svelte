<script>
    let addItem = false;
    let page = "base";
    let editPageData;
    let errorMessageVisible = false;
    let errorMessage;
    let data;
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
    async function getEditPageData() {
        const res = await fetch("/getEditPageData");
        editPageData = await res.json();
        data = JSON.parse(JSON.stringify(editPageData));
        console.log(editPageData);
        return true;
    }

    async function saveData(i, data) {
        console.log(data);
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
        })
            .then((res) => res.json())
            .then((res) => {
                console.log(res);
                if (res.showError) {
                    errorMessageVisible = true;
                    errorMessage = `There was a problem while editing the item: ${res.result}`;
                }
                getEditPageData();
            });
    }

    async function addData() {
        let dataToSend;
        switch (page) {
            case "Users":
                dataToSend = {
                    username: document.getElementById("users_username").value,
                    password: document.getElementById("users_password").value,
                    userType: document.getElementById("users_userType").value,
                };
                break;
            case "Nav":
                dataToSend = {
                    item: document.getElementById("headerItems_item").value,
                };
                break;
            case "Slider":
                dataToSend = {
                    imageUrl: document.getElementById("sliderItems_imageUrl")
                        .value,
                    title: document.getElementById("sliderItems_title").value,
                    description: document.getElementById(
                        "sliderItems_description"
                    ).value,
                    interval: document.getElementById("sliderItems_interval")
                        .value,
                };
                break;
            case "News":
                dataToSend = {
                    header: document.getElementById("news_header").value,
                    title: document.getElementById("news_title").value,
                    content: document.getElementById("news_content").value,
                    article: document.getElementById("news_article").value,
                    buttonText:
                        document.getElementById("news_buttonText").value,
                };
                break;
            case "Cards":
                dataToSend = {
                    title: document.getElementById("contentCards_title").value,
                    subtitle: document.getElementById("contentCards_subtitle")
                        .value,
                    content: document.getElementById("contentCards_content")
                        .value,
                    imageURL: document.getElementById("contentCards_imageURL")
                        .value,
                    isImageOnLeftSide: document.getElementById(
                        "contentCards_isImageOnLeftSide"
                    ).checked,
                };
                break;
            case "Footer":
                dataToSend = {
                    item: document.getElementById("footerItems_item").value,
                };
                break;
            default:
                return "Wrong page id";
        }
        const res = await fetch("/addData", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                dataType: page,
                data: dataToSend,
            }),
        })
            .then((res) => res.json())
            .then((res) => {
                console.log(res);
                if (res.showError) {
                    errorMessageVisible = true;
                    errorMessage = `There was a problem while adding the item: ${res.result}`;
                } else addItem = false;
                getEditPageData();
            });
    }

    async function deleteData(key) {
        if (confirm("Are you sure you want to delete this?")) {
            const res = await fetch("/deleteData", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({
                    dataType: page,
                    key: key,
                }),
            }).then((res) => {
                console.log(res);
                getEditPageData();
            });
        }
    }

    var r = document.querySelector(":root");
    r.style.setProperty("--data-mainBackgroundColor", "#333");
    r.style.setProperty("--data-secondaryBackgroundColor", "#ddd");
    r.style.setProperty("--data-newsHeaderBackgroundColor", "#999");
    r.style.setProperty("--data-mainTextColor", "#ddd");
    r.style.setProperty("--data-secondaryTextColor", "#000");
</script>

<nav id="editNav">
    {#if sessionStorage.userType == "admin"}
        <div
            class="flexCenter"
            on:click={() => SetPage("Users")}
            id="selectUsers"
        >
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
        <div
            class="flexCenter"
            on:click={() => SetPage("News")}
            id="selectNews"
        >
            News
        </div>
        <div
            class="flexCenter"
            on:click={() => SetPage("Cards")}
            id="selectCards"
        >
            Cards
        </div>
        <div
            class="flexCenter"
            on:click={() => SetPage("Footer")}
            id="selectFooter"
        >
            Footer
        </div>
        <div class="flexCenter" on:click={() => SetPage("base")}>Raw data</div>
    {:else if sessionStorage.userType == "moderator"}
        <div
            class="flexCenter"
            on:click={() => SetPage("Slider")}
            id="selectSlider"
        >
            Slider
        </div>
        <div
            class="flexCenter"
            on:click={() => SetPage("News")}
            id="selectNews"
        >
            News
        </div>
        <div
            class="flexCenter"
            on:click={() => SetPage("Cards")}
            id="selectCards"
        >
            Cards
        </div>
    {:else}
        <p
            style="align-self:center; justify-self:center; width:100%; text-align:center;"
        >
            Only moderators and admins can edit the page data
        </p>
    {/if}
    <a class="flexCenter" href="/#/">Back</a>
</nav>

{#await getEditPageData()}
    Waiting for data...
{:then}
    <main class="flexCenter" id="editMain">
        {#if page == "base"}
            <pre>{JSON.stringify(data, null, 2)}</pre>
        {:else if page == "Users"}
            <button class="editPageButton" on:click={() => (addItem = !addItem)}
                >{addItem ? "Back to editing" : "Add new user"}</button
            >
            <div id="userEditForms" class="editForms">
                {#if addItem}
                    <div class="flexCenter flexDirCol editPageForm">
                        <div class="flexSpaceBetween">
                            Username:
                            <input type="text" id="users_username" />
                        </div>
                        <div class="flexSpaceBetween">
                            Password:
                            <input type="password" id="users_password" />
                        </div>
                        <div class="flexSpaceBetween">
                            UserType:
                            <select id="users_userType">
                                <option value="admin">Administrator</option>
                                <option value="moderator">Moderator</option>
                                <option value="user">Basic user</option>
                            </select>
                        </div>
                        <button
                            class="editPageSaveButton"
                            on:click={() => addData()}>Add</button
                        >
                    </div>
                {:else}
                    {#each editPageData.users as user, i}
                        <div class="flexCenter flexDirCol editPageForm">
                            <div class="flexSpaceBetween">
                                Username:
                                <input type="text" bind:value={user.username} />
                            </div>
                            <div class="flexSpaceBetween">
                                Password:
                                <input
                                    type="password"
                                    bind:value={user.password}
                                />
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
                            <button
                                class="editPageDeleteButton"
                                on:click={() =>
                                    deleteData(data.users[i].username)}
                                >Delete</button
                            >
                        </div>
                    {/each}
                {/if}
            </div>
        {:else if page == "Nav"}
            <button class="editPageButton" on:click={() => (addItem = !addItem)}
                >{addItem ? "Back to editing" : "Add new nav item"}</button
            >
            <div id="headerEditForms" class="editForms">
                {#if addItem}
                    <div class="flexCenter flexDirCol editPageForm">
                        <div class="flexSpaceBetween">
                            Item:
                            <input type="text" id="headerItems_item" />
                        </div>
                        <button
                            class="editPageSaveButton"
                            on:click={() => addData()}>Add</button
                        >
                    </div>
                {:else}
                    {#each editPageData.headerItems as headerItem, i}
                        <div class="flexCenter flexDirCol editPageForm">
                            <div class="flexSpaceBetween">
                                Item:
                                <input
                                    type="text"
                                    bind:value={headerItem.item}
                                />
                            </div>
                            <button
                                class="editPageSaveButton"
                                on:click={() => saveData(i, data)}>Save</button
                            >
                            <button
                                class="editPageDeleteButton"
                                on:click={() =>
                                    deleteData(data.headerItems[i].item)}
                                >Delete</button
                            >
                        </div>
                    {/each}
                {/if}
            </div>
        {:else if page == "Slider"}
            <button class="editPageButton" on:click={() => (addItem = !addItem)}
                >{addItem ? "Back to editing" : "Add new slider item"}</button
            >
            <div id="sliderEditForms" class="editForms">
                {#if addItem}
                    <div class="flexCenter flexDirCol editPageForm">
                        <div class="flexSpaceBetween">
                            Title:
                            <input type="text" id="sliderItems_title" />
                        </div>
                        <div class="flexSpaceBetween">
                            Image URL:
                            <input type="text" id="sliderItems_imageUrl" />
                        </div>
                        <div class="flexSpaceBetween">
                            Description:
                            <input id="sliderItems_description" />
                        </div>
                        <div class="flexSpaceBetween">
                            Interval:
                            <input
                                type="number"
                                min="0"
                                max="100000"
                                id="sliderItems_interval"
                            />
                        </div>
                        <button
                            class="editPageSaveButton"
                            on:click={() => addData()}>Add</button
                        >
                    </div>
                {:else}
                    {#each editPageData.sliderItems as sliderItem, i}
                        <div class="flexCenter flexDirCol editPageForm">
                            <div class="flexSpaceBetween">
                                Title:
                                <input
                                    type="text"
                                    bind:value={sliderItem.title}
                                />
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
                            <button
                                class="editPageDeleteButton"
                                on:click={() =>
                                    deleteData(data.sliderItems[i].title)}
                                >Delete</button
                            >
                        </div>
                    {/each}
                {/if}
            </div>
        {:else if page == "News"}
            <button class="editPageButton" on:click={() => (addItem = !addItem)}
                >{addItem ? "Back to editing" : "Add new news"}</button
            >
            <div id="newsEditForms" class="editForms">
                {#if addItem}
                    <div class="flexCenter flexDirCol editPageForm">
                        <div class="flexSpaceBetween">
                            Title:
                            <input type="text" id="news_title" />
                        </div>
                        <div class="flexSpaceBetween">
                            Header:
                            <input type="text" id="news_header" />
                        </div>
                        <div class="flexSpaceBetween">
                            Content:
                            <textarea id="news_content" />
                        </div>
                        <div class="flexSpaceBetween">
                            Article:
                            <textarea id="news_article" />
                        </div>
                        <div class="flexSpaceBetween">
                            Button text:
                            <input type="text" id="news_buttonText" />
                        </div>
                        <button
                            class="editPageSaveButton"
                            on:click={() => addData()}>Add</button
                        >
                    </div>
                {:else}
                    {#each editPageData.news as newsItem, i}
                        <div class="flexCenter flexDirCol editPageForm">
                            <div class="flexSpaceBetween">
                                Title:
                                <input
                                    type="text"
                                    bind:value={newsItem.title}
                                />
                            </div>
                            <div class="flexSpaceBetween">
                                Header:
                                <input
                                    type="text"
                                    bind:value={newsItem.header}
                                />
                            </div>
                            <div class="flexSpaceBetween">
                                Content:
                                <textarea bind:value={newsItem.content} />
                            </div>
                            <div class="flexSpaceBetween">
                                Article:
                                <textarea bind:value={newsItem.article} />
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
                            <button
                                class="editPageDeleteButton"
                                on:click={() => deleteData(data.news[i].title)}
                                >Delete</button
                            >
                        </div>
                    {/each}
                {/if}
            </div>
        {:else if page == "Cards"}
            <button class="editPageButton" on:click={() => (addItem = !addItem)}
                >{addItem ? "Back to editing" : "Add new card"}</button
            >
            <div id="cardsEditForms" class="editForms">
                {#if addItem}
                    <div class="flexCenter flexDirCol editPageForm">
                        <div class="flexSpaceBetween">
                            Title:
                            <input type="text" id="contentCards_title" />
                        </div>
                        <div class="flexSpaceBetween">
                            Subtitle:
                            <input type="text" id="contentCards_subtitle" />
                        </div>
                        <div class="flexSpaceBetween">
                            Image Url:
                            <input type="text" id="contentCards_imageURL" />
                        </div>
                        <div class="flexSpaceBetween">
                            Content:
                            <textarea id="contentCards_content" />
                        </div>
                        <div class="flexSpaceBetween">
                            Is On Left Side:
                            <input
                                type="checkbox"
                                id="contentCards_isImageOnLeftSide"
                            />
                        </div>

                        <button
                            class="editPageSaveButton"
                            on:click={() => addData()}>Add</button
                        >
                    </div>
                {:else}
                    {#each editPageData.contentCards as contentCard, i}
                        <div class="flexCenter flexDirCol editPageForm">
                            <div class="flexSpaceBetween">
                                Title:
                                <input
                                    type="text"
                                    bind:value={contentCard.title}
                                />
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
                            <button
                                class="editPageDeleteButton"
                                on:click={() =>
                                    deleteData(data.contentCards[i].title)}
                                >Delete</button
                            >
                        </div>
                    {/each}
                {/if}
            </div>
        {:else if page == "Footer"}
            <button class="editPageButton" on:click={() => (addItem = !addItem)}
                >{addItem ? "Back to editing" : "Add new footer item"}</button
            >
            <div id="footerEditForms" class="editForms">
                {#if addItem}
                    <div class="flexCenter flexDirCol editPageForm">
                        <div class="flexSpaceBetween">
                            Item:
                            <input type="text" id="footerItems_item" />
                        </div>
                        <button
                            class="editPageSaveButton"
                            on:click={() => addData()}>Add</button
                        >
                    </div>{:else}
                    {#each editPageData.footerItems as footerItem, i}
                        <div class="flexCenter flexDirCol editPageForm">
                            <div class="flexSpaceBetween">
                                Item:
                                <input
                                    type="text"
                                    bind:value={footerItem.item}
                                />
                            </div>
                            <button
                                class="editPageSaveButton"
                                on:click={() => saveData(i, data)}>Save</button
                            >
                            <button
                                class="editPageDeleteButton"
                                on:click={() =>
                                    deleteData(data.footerItems[i].item)}
                                >Delete</button
                            >
                        </div>
                    {/each}
                {/if}
            </div>
        {:else}
            Something went wrong
        {/if}
    </main>
    {#if errorMessageVisible}
        <div id="errorMessage">
            {errorMessage}
            <button
                id="closeErrorMessageButton"
                on:click={() => (errorMessageVisible = false)}>&#10006;</button
            >
        </div>
    {/if}
{/await}
