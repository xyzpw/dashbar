# dashbar
[![Downloads](https://static.pepy.tech/badge/dashbar)](https://pepy.tech/project/dashbar)<br>
A progress-bar designed to be useful and easy to use.
![dashbar-demo-preview](https://github.com/xyzpw/dashbar/assets/76017734/d5a3bd52-2bc5-455d-ba63-fe28249defe8)

# Usage
Firstly, you need to import `dashbar`.<br>
It will be useful to import the `time` module as well
```python
import dashbar, time
```
## Iterating
To start dashbar, follow the example code below:
```python
for i in dashbar.dash(10, dash_type="pipe", desc="example"):
    time.sleep(1/10) #completion after one second
    if i == 5:
        dashbar.status("half-way complete")
```
If the progress is large, the `autodash` function can be used, which adjusts the step count to fit the terminal.
```python
for i in dashbar.autodash(10):
    time.sleep(1/10)
    if i == 8:
        dashbar.log("eighty percent complete")
```
## Customizing dashbar
Dashbars can be customized by the following code:
```python
dashbar.customize(element="filler", value=" ")
```
List of dashbars:
- classic
- arrow
- box
- circle_charger
- box_charger
- striped
- dollar
- box_shade
- pipe
- custom

List of dashbar elements:
- start
- head
- trail
- filler
- finish
## Building a Dashbar
Dashbars can be built via the `Build` class.
```python
bar = dashbar.Build(10, "box_shade")
for i in range(100):
    if i%10 == 0:
        bar.update(1, display=True)
    time.sleep(1/20) #completion after five seconds
```
