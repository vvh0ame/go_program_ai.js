# go_program_ai.js
Web-API for [goprogram.ai](https://goprogram.ai) that generates quotes to motivate or inspire you!

## Example
```JavaScript
async function main() {
	const { GoProgramAi } = require("./go_program_ai.js")
	const goProgramAi = new GoProgramAi()
	const inspirationQuote = await goProgramAi.getInspirationQuote()
	console.log(inspirationQuote)
}

main()
```
