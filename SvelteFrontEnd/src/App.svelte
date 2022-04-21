<script>
	import loginPage from "./routes/loginPage.svelte";
	import registerPage from "./routes/registerPage.svelte";
	import mainPage from "./routes/mainPage.svelte";
	import editPage from "./routes/editPage.svelte";
	import Tailwindcss from "./Tailwindcss.svelte";
	import Router from "svelte-spa-router";
</script>

<Tailwindcss />

<Router
	routes={{
		"/": mainPage,
		"/registerPage": registerPage,
		"/logInPage": loginPage,
		"/editPage": editPage,
	}}
/>
<main />
