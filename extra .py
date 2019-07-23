 # company name vendor
     #   cnVendor = self.driver.find_element_by_xpath("//XCUIElementTypeOther[@name=\"Company name for PM profile\"]/XCUIElementTypeOther")
    ####    self.assertEqual(firstname[0].get_attribute("value"), "lol")
     ######   xyz = firstname[0].get_attribute("value")
       ## print(xyz)
     ####   print("equal")
     #####   sleep(1)
        # close the keyboard
      #  TouchAction(self.driver).tap(x=65, y=430).perform()
      #  sleep(1)
      #  print("close the keyboard")
        # swipe1
      #  TouchAction(self.driver).press(x=245, y=531).move_to(x=239, y=99).release().perform()
      #  sleep(1)
      #  print("swipe 1")
        # swipe 2
    # TouchAction(self.driver).press(x=245, y=531).move_to(x=239, y=99).release().perform()
    #    sleep(1)  
    #----------------------
     #   actions = TouchAction(self.driver)
       # actions.scroll_from_element(emailTF, 175, 185)
       # print("scrool from element")
      #  actions.scroll(175, 575)
     #   print("scroll")
      #  actions.perform()

     #-----------------
      # alert
      #size = self.driver.manage().window().getSize()
  # starty = (size.height * 0.80)
  # endy = (int) (size.height * 0.20)
  # startx = size.width / 2
  # self.driver.swipe(startx, starty, startx, endy, 2000) 


 #   print("swipe 2")
        # swipe upto submit button
     #  TouchAction(self.driver)   .press(x=262, y=599)   .move_to(x=257, y=220)   .release()   .perform()
      # TouchAction(self.driver)   .press(x=214, y=583)   .move_to(x=224, y=418)   .release()   .perform()
        print("swipe@")
        TouchAction(self.driver)   .press(x=188, y=312)   .move_to(x=176, y=578)   .release()   .perform()
        sleep(1)
        TouchAction(self.driver)   .press(x=204, y=423)   .move_to(x=200, y=134)   .release()   .perform()
        print("new swipe")
        print("swipe2")
        TouchAction(self.driver).press(x=188, y=312).move_to(x=176, y=578).release().perform()
        sleep(1)
        TouchAction(self.driver).press(x=204, y=423).move_to(x=200, y=134).release().perform()
        print("stripe 3")
        sleep(2)
        submit = self.driver.find_element_by_accessibility_id("Submit")
        print("submit before")
        TouchAction(self.driver).press(firstname[0]).move_to(submit).release().perform()
        print("stripe 3")
        sleep(2)
       # TouchAction(self.driver)   .press(x=180, y=426)   .move_to(x=181, y=306)   .release()   .perform()
       # TouchAction(self.driver)   .press(x=267, y=466)   .move_to(x=269, y=249)   .release()   .perform()
       # sleep(1)


        self.driver.scroll(firstname[0], phoneNo[0])
        print("new scrol")
        sleep(1)
        self.driver.scroll(phoneNo[0], cnVendor)
        print("scroll2")
        sleep(1)