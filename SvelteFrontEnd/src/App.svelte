<script>
	import loginPage from "./routes/loginPage.svelte";
	import Tailwindcss from "./Tailwindcss.svelte";
	import Router from "svelte-spa-router";
  </script>
  
  <Tailwindcss />
  
  <Router
	routes={{
	  "/": loginPage
	}}
  />
  <main />
  