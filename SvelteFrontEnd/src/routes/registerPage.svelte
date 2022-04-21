<script>
    let registerStatus = ""
    async function register() {
        let username = document.getElementById("username").value;
        let password = document.getElementById("password").value;
        console.log(username, password);
        if (username == "" || password == "") {
            return;
        }
        if (
            username.replace(" ", "") == "" ||
            password.replace(" ", "") == ""
        ) {
            return;
        }
        if (
            username.replace(" ", "") != username ||
            password.replace(" ", "") != password
        ) {
            return;
        }
        let body = JSON.stringify({
            username: document.getElementById("username").value,
            password: document.getElementById("password").value,
        });
        console.log(body);
        await fetch("/register", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                username: document.getElementById("username").value,
                password: document.getElementById("password").value,
            }),
        })
            .then((response) => response.json())
            .then((data) => {
                console.log(data, data.loggedIn);
                registerStatus = data.message
            });
    }
</script>

<div class="centerDiv">
    <h1>CMS Project</h1>
    <div class="loginForm">
        <label for="username">Username</label>
        <input id="username" name="username" type="text" />
        <label for="password">Password</label>
        <input id="password" name="password" type="password" />
        <div id="loginPageBtns">
            <input type="submit" class="aAsButton" value="Register" on:click={register} />
            <a href="/#/logInPage" class="secondaryBtn">Log In</a>
        </div>
        <p style="width:90%; text-align:center; text-decoration:underline;" class="{registerStatus == '' ? "hidden" : ""}">{registerStatus}</p>
    </div>
</div>
