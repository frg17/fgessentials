using System;
using System.Threading;
using Gtk;

public class FGMain {
    static Label myLabel = null;

    public static int updateLabel(string str) {
        myLabel.Text = str;
        return 0;
    }
	
	public static void Main() {
        Application.Init();

        //Create the window.
        Window myWin = new Window("FrozenApp");
        myWin.Resize(400, 400);

        myLabel = new Label();
        myLabel.Text = "Hello World!!!";

        UDPListener.Del del = updateLabel;
        Thread t = new Thread(UDPListener.StartListener);
        t.Start(del);
        //Add the label to the form.
        myWin.Add(myLabel);

        //Show everything.
        myWin.ShowAll();

        Application.Run();

	}
}



