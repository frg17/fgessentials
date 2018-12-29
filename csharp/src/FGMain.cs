using System;
using System.Threading;
using Gtk;

public class FGMain {
    static Label myLabel = null;

    public static int updateLabel(string str) {
        myLabel.Text = str;
        return 0;
    }

    private static void deleteHandler(object obj, DeleteEventArgs args) {
        Environment.Exit(0);
    }
	
	public static void Main() {
        var configHandler = new FGSharp.Utility.ConfigHandler();

        int sum = configHandler.GetInt("shi") + configHandler.GetInt("shi2");
        Application.Init();

        //Create the window.
        Window myWin = new Window("FrozenApp");
        myWin.Resize(400, 400);

        myLabel = new Label();
        myLabel.Text = configHandler.GetString("shakeit") + sum.ToString();

        UDPListener.Del del = updateLabel;
        Thread t = new Thread(UDPListener.StartListener);
        t.Start(del);
        //Add the label to the form.
        myWin.Add(myLabel);
        myWin.DeleteEvent += deleteHandler;

        //Show everything.
        myWin.ShowAll();

        Application.Run();

	}
}



