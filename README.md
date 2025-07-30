# magic 🪄
MATLAB Magic square deployed as Python Package📦

## Install MATLAB Magic square as Python Package

```
pip install "git+https://github.com/yanndebray/magic.git@main#egg=mdeploy-r2024b&subdirectory=mdeployPythonPackage24b/output/build"
```

## Call from Python

```
>>> import mdeploy
>>> m = mdeploy.initialize()
>>> m.mymagic(3)
matlab.double([[8.0,1.0,6.0],[3.0,5.0,7.0],[4.0,9.0,2.0]])
```

## Deploy as a Streamlit app 🚀

https://github.com/user-attachments/assets/cea78f62-192e-42a2-beac-3f25a179cf42

## Host on Render

*free instances will spin down with inactivity, which can delay requests by 50 seconds or more.*

Services:
- FrontEnd: https://streamlit-ph66.onrender.com
- BackEnd: https://matlab-0j1h.onrender.com ([Health API](https://matlab-0j1h.onrender.com/api/health))

![render](img/render.png)