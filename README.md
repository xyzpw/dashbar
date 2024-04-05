# dashbar
![PyPI - Version](https://img.shields.io/pypi/v/dashbar)
![Pepy Total Downloads](https://img.shields.io/pepy/dt/dashbar?color=red)
![GitHub repo size](https://img.shields.io/github/repo-size/xyzpw/dashbar)<br/><br/>
A progress-bar designed to be useful and easy to use.<br/><br/>
![dashbar-demo-preview](https://github.com/xyzpw/dashbar/assets/76017734/d5a3bd52-2bc5-455d-ba63-fe28249defe8)
## Usage
### Iterating
To start dashbar, execute the following code:
```python
for i in dashbar.dash(10, dash_type="pipe", desc="example"):
    time.sleep(1/10) #completion after one second
    if i == 5:
        dashbar.status("half-way complete")
```
If the progress is large, the `autodash` function can be used, which adjusts the step count to fit the terminal:
```python
for i in dashbar.autodash(10):
    time.sleep(1/10)
    if i == 8:
        dashbar.log("eighty percent complete")
```

### Customizing dashbar
Dashbars can be customized with the following code:
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
- heart
- radioactive
- custom

List of dashbar elements:
- start
- head
- trail
- filler
- finish

### Building a Dashbar
Dashbars can be built via the `Dashbar` class:
```python
bar = dashbar.Dashbar(10, "box_shade")
for i in range(100):
    if i%10 == 0:
        bar.update(1, display=True)
    time.sleep(1/20) #completion after five seconds
```
