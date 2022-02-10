/// <reference types="cypress" />

 
// https://apps.jll.com/PortfolioTracker/OneView/Editor.aspx?nClientID=6503&nType=0&nActivityType=0&nLeaseID=17648522&nParentClientID=0&nParentLeaseID=0&sSortOrder=&sAscDesc=ASC&PageID=1&status=

/*
// https://apps.jll.com/PortfolioTracker/OneView/Editor.aspx?
nClientID=6503&
nType=0&
nActivityType=0&
nLeaseID=17648522&
nParentClientID=0&
nParentLeaseID=0&
sSortOrder=&
sAscDesc=ASC&
PageID=1&status=

*/
const username = "gordon.tang"
const password = "UZAevt8$"


const ovcpid = 17648522
const google = "https://www.google.com/"
const phub = `https://apps.jll.com/PortfolioTracker/OneView/Editor.aspx?nClientID=6503&nType=0&nActivityType=0&nLeaseID=${ovcpid}&nParentClientID=0&nParentLeaseID=0&sSortOrder=&sAscDesc=ASC&PageID=1&status=`

//   beforeEach(function(){
//     cy.visit(google)
// })

// input-validation-error inp inp-usr
// input-validation-error inp inp-pwd sso-hid

describe("Correct Street", function () {
    
/*
beforeEach(
    ()=>{
        cy.visit(phub)
    }
)
*/

it('test visit method', function() {
    cy.visit(phub)
  })

})
