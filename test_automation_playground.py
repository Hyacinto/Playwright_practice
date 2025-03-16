from playwright.sync_api import TimeoutError as PlaywrightTimeoutError
import pyperclip

# Scenario 1:

# Record button click.
# Then execute your test to make sure that ID is not used for button identification.

def test_dynamic_ID(setup_teardown):
    page = setup_teardown

    page.click("text=Dynamic ID")
    page.wait_for_selector(".navbar-brand")

    button = page.get_by_role("button", name="Button with Dynamic ID") #ARIA-rolle
    button.click()

    # Is the button focused?
    assert button.evaluate("el => document.activeElement === el") == True

# Scenario 2:

# Record primary (blue) button click and press ok in alert popup.
# Then execute your test to make sure that it can identify the button using btn-primary class.

def test_class_attribute(setup_teardown):
    page = setup_teardown

    page.click("text=Class Attribute")
    page.wait_for_selector(".navbar-brand")

    button = page.locator("//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]") #The XPATH expression came from the page
    button.click()

    def handle_dialog(dialog):
        dialog_type = dialog.type
        dialog.accept()
        assert dialog_type == "alert"
        
    page.on('dialog', handle_dialog)

# Scenario 3:

# Record button click and then duplicate the button click step in your test.
# Execute the test to make sure that green button can not be hit twice.

def test_hidden_layers(setup_teardown):
    page = setup_teardown

    page.click("text=Hidden Layers")
    page.wait_for_selector(".navbar-brand")

    button = page.get_by_role("button", name="Button")
    button.click()
    try:
        button.click()
    except Exception as e:
        assert 'Locator.click: Error: strict mode violation: get_by_role("button", name="Button") resolved to 2 elements:' in str(e)

# Scenario 4:

# Navigate to Home page and record Load Delays link click and button click on this page.
# Then play the test. It should wait until page is loaded.

def test_load_delays(setup_teardown):
    page = setup_teardown

    page.click("text=Load Delay")
    page.wait_for_selector(".navbar-brand")

    button = page.get_by_role("button", name="Button Appearing After Delay")
    button.click()

    assert button.evaluate("el => document.activeElement === el") == True

# Scenario 5:

# Record the following steps. Press the button below and wait for data to appear (15 seconds), click on text of the loaded label.
# Then execute your test to make sure it waits for label text to appear.


def test_AJAX_Data(setup_teardown):
    page = setup_teardown

    page.click("text=AJAX Data")
    page.wait_for_selector(".navbar-brand")

    button = page.get_by_role("button", name="Button Triggering AJAX Request")
    button.click()

    message = page.wait_for_selector(".bg-success")

    is_visible = message.is_visible()

    message.click()

    assert is_visible == True

# Scenario 6:

# Record the following steps. Press the button below and wait for data to appear (15 seconds), click on text of the loaded label.
# Then execute your test to make sure it waits for label text to appear.

def test_client_side_delay(setup_teardown):
    page = setup_teardown

    page.click("text=Client Side Delay")
    page.wait_for_selector(".navbar-brand")

    button = page.get_by_role("button", name="Button Triggering Client Side Logic")
    button.click()

    message = page.wait_for_selector(".bg-success")

    is_visible = message.is_visible()

    message.click()

    assert is_visible == True

# Scenario 7:

# Record button click. The button becomes green after clicking.
# Then execute your test to make sure that it is able to click the button.

def test_click(setup_teardown):
    page = setup_teardown
    
    page.click("text=Click")
    page.wait_for_selector(".navbar-brand")

    button = page.get_by_role("button", name="Button That Ignores DOM Click Event")
    button.click()

    page.wait_for_timeout(2000)
        
    button = page.get_by_role("button", name="Button That Ignores DOM Click Event")
    background_color = button.evaluate("el => window.getComputedStyle(el).backgroundColor")

    assert background_color == "rgb(33, 136, 56)"

# Scenario 8:

# Record setting text into the input field and pressing the button.
# Then execute your test to make sure that the button name is changing.

def test_text_input(setup_teardown):
    page = setup_teardown

    page.click("text=Text Input")
    page.wait_for_selector(".navbar-brand")

    input_field = page.get_by_role("textbox", name="Set New Button Name")
    input_field.click()
    input_field.fill("MyButt")

    button = page.get_by_role("button", name="Button That Should Change it'")
    button.click()

    button = page.locator("#updatingButton")

    assert button.evaluate("el => el.innerText") == "MyButt"

# Scenario 9:

# Find a button in the scroll view and record button click.
# Update your test to automatically scroll the button into a visible area.
# Then execute your test to make sure it works.

def test_scrollbars(setup_teardown):
    page = setup_teardown

    page.click("text=Scrollbars")
    page.wait_for_selector(".navbar-brand")

    button = page.get_by_role("button", name="Hiding Button")
    button.click()

    assert button.evaluate("el => document.activeElement === el") == True

# Scenario 10:

# For Chrome process get value of CPU load.
# Compare it with value in the yellow label.

def test_dynamic_table(setup_teardown):
    page = setup_teardown

    page.click("text=Dynamic Table")
    page.wait_for_selector(".navbar-brand")
    
    # 1. Find the index of the column in the header
  
    column_headers = page.locator("div[role='rowgroup'] div[role='row']:nth-child(1) span[role='columnheader']")
    headers = column_headers.all_text_contents()
    column_index = headers.index("CPU")

    # 2. Find the row index based on the first column

    all_rowgroups = page.locator("div[role='rowgroup']").all()
    
    target_row = None

    for rowgroup in all_rowgroups:
        rows = rowgroup.locator("div[role='row']").all()
        for row in rows:
            cells = row.locator("span[role='cell']").all()
            if cells and cells[0].text_content().strip() == "Chrome":
                target_row = cells
                break
        if target_row:
            break

    # 3. Find the specific cell in the table
 
    cell_text = target_row[column_index].text_content()

    message = page.locator(".bg-warning")
    message_text = message.evaluate("el => el.textContent").replace("Chrome CPU: ", "")

    assert cell_text == message_text

# Scenario 11:

# Create a test that finds an element with Welcome... text.

def test_verify_text(setup_teardown):
    page = setup_teardown

    page.click("text=Verify Text")
    page.wait_for_selector(".navbar-brand")

    message = page.locator("//span[normalize-space(.)='Welcome UserName!']")
    message_text = message.evaluate("el => el.textContent").strip()

    text = 'Welcome UserName!'

    assert message_text == text

# Scenario 12:

# Create a test that clicks Start button and then waits for the progress bar to reach 75%. 
# Then the test should click Stop. The less the differnce between value of the stopped progress bar and 75% the better your result.

def test_progress_bar(setup_teardown):
    page = setup_teardown

    page.click("text=Progress Bar")
    page.wait_for_selector(".navbar-brand")

    page.get_by_role("button", name="Start").click()
    
    page.get_by_role("button", name="Start")

    progress_bar = page.locator("div").filter(has_text="%").nth(1)
    progress = ""

    while progress != "74%":
        progress = progress_bar.evaluate("el => el.textContent").strip()

    page.get_by_role("button", name="Stop").click()

    result_element = page.locator('#result')
    result_text = result_element.evaluate("el => el.textContent").strip().split()

    result = int(result_text[1].replace(",",""))

    assert (result < 2) == True

# Scenario 13:

# Learn locators of all buttons.
# In your testing scenario press Hide button.
# Determine if other buttons visible or not.

def test_visibility(setup_teardown):
    page = setup_teardown

    page.click("text=Visibility")
    page.wait_for_selector(".navbar-brand")

    offscreen = page.get_by_role("button", name="Offscreen")
    overlapped = page.get_by_role("button", name="Overlapped")
    zero_width = page.get_by_role("button", name="Zero Width")
    display_none = page.get_by_role("button", name="Display None")
    visibility_hidden = page.get_by_role("button", name="Visibility Hidden")
    removed = page.get_by_role("button", name="Removed")
    opacity = page.get_by_role("button", name="Opacity")
    hide = page.get_by_role("button", name="Hide")

    hide.click()
    
    clickable = True
    try:
            overlapped.click().timeout(2000)
    except PlaywrightTimeoutError:
        clickable = False
    

    box = offscreen.bounding_box()
    assert box is None or box["x"] < 0  # If there is no bounding box, or the coordinate is negative, the element is hidden
    assert not clickable
    assert zero_width.bounding_box()["width"] == 0
    assert display_none.is_hidden()
    assert visibility_hidden.is_hidden()
    assert removed.count() == 0 
    assert opacity.evaluate("el => getComputedStyle(el).opacity") == "0"
    assert hide.is_visible()

# Scenario 14:

# Fill in and submit the form. 
# For successfull login use any non-empty user name and `pwd` as password.

def test_sample_app(setup_teardown):
    page = setup_teardown

    page.click("text=Sample App")
    page.wait_for_selector(".navbar-brand")

    page.get_by_role("textbox", name="User Name").click()
    page.get_by_role("textbox", name="User Name").fill("Hyacinto")
    page.get_by_role("textbox", name="********").click()
    page.get_by_role("textbox", name="********").fill("pwd")
    page.get_by_role("button", name="Log In").click()

    message = page.locator("div").filter(has_text="Welcome, Hyacinto!").nth(2)

    assert message.is_visible

# Scenario 15:

# Record 2 consecutive link clicks.
# Execute the test and make sure that click count is increasing by 2.

def test_mouse_over(setup_teardown):
    page = setup_teardown

    page.click("text=Mouse Over")
    page.wait_for_selector(".navbar-brand")

    click_me_button = page.get_by_text("Click me")
    click_me_button.hover()

    click_me_button.click()
    click_me_button.click()

    link_button = page.get_by_text("Link Button")
    link_button.hover()

    link_button.click()
    link_button.click()


    click_me_button_counter = int(page.locator("#clickCount").text_content())
    link_button_counter = int(page.locator("#clickButtonCount").text_content())

    assert click_me_button_counter == 2
    assert link_button_counter == 2

# Scenario 16:

# Use the following xpath to find the button in your test:
# //button[text()='My Button']
# Notice that the XPath does not work. Change the space between 'My' and 'Button' to a non-breaking space. This time the XPath should be valid.

def test_non_breaking_space(setup_teardown):
    page = setup_teardown

    page.click("text=Non-Breaking Space")
    page.wait_for_selector(".navbar-brand")

    button_without_nbsp = page.locator("//button[text()='My Button']")

    clickable = True
    
    try:
        button_without_nbsp.click().timeout(2000)
    except PlaywrightTimeoutError:
        clickable = False
    
    button_with_nbsp = page.locator("//button[text()='My\u00A0Button']")
    button_with_nbsp.click()

    assert not clickable
    assert button_with_nbsp.evaluate("el => document.activeElement === el") == True

# Scenario 17:

# Record setting text into the Name input field (scroll element before entering the text).
# Then execute your test to make sure that the text was entered correctly.

def test_overlapped_element(setup_teardown):
    page = setup_teardown

    page.click("text=Overlapped Element")
    page.wait_for_selector(".navbar-brand")

    page.get_by_role("textbox", name="Id").click()
    page.get_by_role("textbox", name="Id").fill("781213")
    page.get_by_role("textbox", name="Name").click()
    name_field = page.get_by_role("textbox", name="Name")
    name_field.fill("Hyacinto")
    name_field.press("Enter")

    assert name_field.input_value() == "Hyacinto"

# Scenario 18:

# Create a test that clicks on ⚙ and then on 📋 buttons. This sequence of steps generates new guid and copies it to the clipboard.
# Add an assertion step to your test to compare the value from the clipboard with the value of the input field.
# Then execute the test to make sure that the assertion step is not failing.

def test_shadow_DOM(setup_teardown):
    page = setup_teardown

    page.click("text=Shadow DOM")
    page.wait_for_selector(".navbar-brand")

    page.locator("#buttonGenerate").click()
    page.locator("#buttonCopy").click()

    field_value = page.locator("#editField").input_value()
    clipboard_value = pyperclip.paste()

    assert field_value == clipboard_value

 # Scenario 19:

 # Record clicks on `Alert`, `Confirm` and `Prompt` buttons. Click `OK` to confirm, answer with non-default value to the prompt.
 # Then execute your test to make sure that it passes completely without manual steps.

def test_alerts(setup_teardown):
    page = setup_teardown

    page.click("text=Alerts")
    page.wait_for_selector(".navbar-brand")

    def handle_dialog(dialog):
        dialog_type = dialog.type
        if dialog_type == "alert" or dialog_type == "confirm":
            dialog.accept()
        else:
            dialog.accept("dog")

    page.on("dialog",handle_dialog)

    page.get_by_role("button", name="Alert").click()

    page.get_by_role("button", name="Confirm").click()

    page.get_by_role("button", name="Prompt").click()

# Scenario 20:

# Attach a file via drag&drop.
# Attach a file using `Browse files` button

def test_file_upload(setup_teardown):
    page = setup_teardown

    page.click("text=File Upload")
    page.wait_for_selector(".navbar-brand")

    page.locator("iframe").content_frame.locator("div").nth(2).evaluate("""
    (dropZone, filePath) => {
        const file = new File([filePath], "drag-drop.txt", { type: "text/plain" });
        const dataTransfer = new DataTransfer();
        dataTransfer.items.add(file);

        const dropEvent = new DragEvent('drop', {
            bubbles: true,
            cancelable: true,
            dataTransfer: dataTransfer
        });
        dropZone.dispatchEvent(dropEvent);
    }
    """, [page.locator("iframe").content_frame.locator("div").nth(2), "./path/to/your/existing-file.txt"])

    page.locator("iframe").content_frame.locator("#browse").set_input_files("./browse-add-file.txt")

    actual_result = int(page.locator("iframe").content_frame.locator(".success-file").locator("p").inner_text().replace(" file(s) selected",""))

    expected_result = 2

    assert actual_result == expected_result

# Scenario 21:

# Record `Start Animation` button click. Wait for animation to complete and record click on `Moving Target`.
# Then execute your test to make sure that when Moving Target is clicked, it's class does not contain 'spin'. 
# The class is printed on the status label below the buttons.

def test_animated_button(setup_teardown):
    page = setup_teardown

    page.click("text=Animated Button")
    page.wait_for_selector(".navbar-brand")

    page.get_by_role("button", name="Start Animation").click()
    page.wait_for_selector("text=Animation done")
    page.get_by_role("button", name="Moving Target").click()
    
    assert page.wait_for_selector("text=Moving Target clicked. It's").is_visible

# Scenario 22:

# Record button click. Also record text input into an edit field.
# Make a test that enters text as soon as the edit field becomes enabled.

def test_disabled_input(setup_teardown):
    page = setup_teardown

    page.click("text=Disabled Input")
    page.wait_for_selector(".navbar-brand")

    page.get_by_role("button", name="Enable Edit Field with 5").click()
    
    page.wait_for_selector("text=Input Enabled...")

    enabled = True

    try:
        page.get_by_role("textbox", name="Edit Field").fill("Enabled")
    except:
        enabled = False

    assert enabled

# Scenario 23:

# Choose an element type from the combobox.
# Check the checkboxes to set the element's properties.
# Then click one of the Apply buttons to immediately apply the settings and restore interactable state of the element after a delay.
# Interact with the element in the Playground section (click, select item, enter text).
# Observe the status messages.

def test_auto_wait(setup_teardown):
    page = setup_teardown

    page.click("text=Auto Wait")
    page.wait_for_selector(".navbar-brand")

    select_options = ["button", "input", "textarea", "select", "label"]

    for i in range(5):
        page.get_by_label("Choose an element type:").select_option(select_options[i])
       
        checkboxes = page.get_by_role("checkbox").all()
        for checkbox in checkboxes:
            checkbox.uncheck()
        
        page.get_by_role("button", name="Apply 10s").click()
        page.wait_for_selector("#target")
        element = page.locator("#target")
        element.click()
    
        initialy_state = page.locator("#opstatus").inner_text()

        try:

            try:    
                element.fill("This is a test text :).")
            except:
                pass

            try:
                element.select_option("Item 2")
            except:
                pass
        
        finally:
            
            page.locator("#opstatus").click()
            changed_state = page.locator("#opstatus").inner_text()

            result = initialy_state == changed_state

            if select_options[i] == "button" or select_options[i] == "label":
                assert result
            else:
                assert not result

            continue


    
    










 





   













  














    




    