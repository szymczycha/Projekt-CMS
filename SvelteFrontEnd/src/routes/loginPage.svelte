<script>
    async function logIn() {
        if (
            document.getElementById("username").value.replace(" ", "") == "" &&
            document.getElementById("password").value.replace(" ", "") == ""
        ) {
            return;
        }
        if (
            document.getElementById("username").value.replace(" ", "") !=
                document.getElementById("username").value &&
            document.getElementById("password").value.replace(" ", "") !=
                document.getElementById("username").value
        ) {
            return;
        }
        await fetch("/logIn", {
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
                if (data.loggedIn == "true") {
                    sessionStorage.setItem("loggedIn", "true");
                    sessionStorage.setItem("userType", data.userType);
                    window.location.href = "/";
                }
                console.log(
                    sessionStorage.getItem("loggedIn"),
                    sessionStorage.getItem("userType")
                );
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
            <button on:click={logIn} class="aAsButton">Log In</button>
            <a href="/#/registerPage" class="secondaryBtn">Register</a>
        </div>
    </div>
</div>
