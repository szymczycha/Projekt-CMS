<script>
	import loginPage from "./routes/loginPage.svelte";
	import registerPage from "./routes/registerPage.svelte";
	import mainPage from "./routes/mainPage.svelte";
	import editPage from "./routes/editPage.svelte";
	import themesEditPage from "./routes/themesEditPage.svelte";
	import gallery from "./routes/gallery.svelte";
	import Tailwindcss from "./Tailwindcss.svelte";
	import Router from "svelte-spa-router";
	import article from "./routes/article.svelte";
</script>

<Tailwindcss />

<Router
	routes={{
		"/": mainPage,
		"/registerPage": registerPage,
		"/logInPage": loginPage,
		"/editPage": editPage,
		"/themesEditPage": themesEditPage,
		"/gallery": gallery,
		"/article": article,
	}}
/>
<main />
