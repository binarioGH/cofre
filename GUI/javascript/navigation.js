

let navigation = document.getElementsByClassName("navop");

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

