const shareButton = document.querySelector(".share-button");
shareButton.addEventListener("click", () => {
  navigator.clipboard.writeText(location.href);
  alert("URL has been copied to clipboard");
});
