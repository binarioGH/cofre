

let navigation = document.getElementsByClassName("navop");

let menunavigation = document.getElementsByClassName("menunav");

for(let nav_button of navigation){
	nav_button.addEventListener("click", function(){
		let get_to = this.getAttribute("goto");
		let page = document.getElementById(get_to);
		let pages = document.getElementsByClassName("page");

		for(article of pages){
			article.style.zIndex = 0;
		}
		page.style.zIndex = 1;
 	})
}

for(let menu_button of menunavigation){
	menu_button.addEventListener("click", function(){
		let get_to = this.getAttribute("goto");
		let page = document.getElementById(get_to);
		let pages = document.getElementsByClassName("container");

		for(article of pages){
			article.style.zIndex = 0;
		}
		page.style.zIndex = 1;
 	})
}


