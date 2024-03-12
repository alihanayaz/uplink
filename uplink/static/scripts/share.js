const shareButton = document.querySelector(".share-button");
const initialText = shareButton.innerHTML;
const link = shareButton.getAttribute("data-link");
shareButton.addEventListener("click", () => {
  navigator.clipboard.writeText(`${location.origin}/user/${link}`);
  shareButton.innerHTML = "Copied!";
  setTimeout(() => {
    shareButton.innerHTML = initialText;
  }, 2000);
});
