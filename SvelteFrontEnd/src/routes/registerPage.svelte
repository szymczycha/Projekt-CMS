<script>
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
        <div style="display: flex; justify-content: space-evenly; width:100%;">
            <input type="submit" value="Register" on:click={register} />
            <a href="/#/logInPage" class="aAsButton">Log In</a>
        </div>
    </div>
</div>
