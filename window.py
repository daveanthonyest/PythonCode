import wx

 

def bnclick(evt):

    print(txt.GetValue())

 

theApp = wx.App()

f = wx.Frame(parent = None, title = "My GUI App")

bn = wx.Button(parent = f, label = "Click Me", size=(50,25))

bn.SetPosition(wx.Point(50,45))
bn.Bind(wx.EVT_BUTTON,bnclick)
 

txt = wx.TextCtrl(parent = f, size = (75, 25))

txt.SetPosition(wx.Point(50, 15))

f.Show()

theApp.MainLoop()