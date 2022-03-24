const puppeteer = require('puppeteer')

const username = "gordon.tang"
const password = "UZAevt8$"


// input.input-validation-error.inp.inp-usr

const phubAutomation = async () => {
    const browser = await puppeteer.launch()
    const page = await browser.newPage()
    const ovcpid = 17648522
    const phub = `https://apps.jll.com/PortfolioTracker/OneView/Editor.aspx?nClientID=6503&nType=0&nActivityType=0&nLeaseID=${ovcpid}&nParentClientID=0&nParentLeaseID=0&sSortOrder=&sAscDesc=ASC&PageID=1&status=`
    
    await page.goto(phub)

    // // input
    // const userInput = await page.waitForSelector('.input-validation-error.inp.inp-usr')
    
    // // .$$('')

    // userInput.focus()

    await page.screenshot({                      // Screenshot the website using defined options
 
        path: "./screenshot.png",                   // Save the screenshot in current directory
     
        fullPage: true                              // take a fullpage screenshot
     
      });

      await browser.close()
    
}
phubAutomation()