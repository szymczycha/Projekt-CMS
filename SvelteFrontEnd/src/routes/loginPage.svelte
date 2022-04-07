<script>
    async function logIn(){
        await fetch("http://127.0.0.1:5000/logIn", {
            method: "POST",
            mode: 'no-cors',
            headers: {
                'Content-Type': 'text/plain'//'application/json'
            },
            body: JSON.stringify({
                username: document.getElementById("username").value,
                password: document.getElementById("password").value
            })
        }).then(response => response.json()).then(data => console.log(data))
    }
</script>

<div class="centerDiv">
    <h1>CMS Project</h1>
    <div class="loginForm">
        <label for="username">Username</label>
        <input id="username" name="username" type="text"/>
        <label for="password">Password</label>
        <input id="password" name="password" type="password"/>
        <div style="display: flex; justify-content: space-evenly; width:100%;">
            <button on:click={logIn}>Log In</button>  
            <a href="/#/registerPage" class="aAsButton">Register</a>
        </div>
    </div>
</div>