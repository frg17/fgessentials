/*
    Ease of use for reading a config file.
    File name is expected by default to be named app.conf and stored
    in root directory. 
*/
namespace FGSharp.Utility {
    public class ConfigHandler {
        private System.Collections.Hashtable configMap; //Map holding config variables.
        private string filepath; //Name/path of config file.

        /**
        *  Constructor has instance use non-defailt file path.
        */
        public ConfigHandler(string filepath) {
            this.filepath = filepath;
            init();
        }

        /**
        *  Constructor has instance use default file path.
        */
        public ConfigHandler() {
            this.filepath = "./app.conf";
            init();
        }

        /**
        *  Initialises ConfigHandler instance, loading config variables.
        */
        private void init() {
            this.configMap = new System.Collections.Hashtable();

            //Read file.
            string text = System.IO.File.ReadAllText(filepath);
            string[] lines = text.Split("\n");

            //Strip file.
            foreach(string l in lines) {
                if(!System.String.IsNullOrWhiteSpace(l)) {
                    string[] key_val = l.Split("=");
                    if(key_val.Length != 2) {
                        throw new System.ArgumentException($"Error reading config file. {l}");
                    } else {
                        this.configMap.Add(key_val[0].Trim(), key_val[1].Trim());
                    }
                }
            }
        }

        /**
        *  Returns a config string corresponding to the given @key.
        */
        public string GetString(string key) {
            if (!configMap.Contains(key))
                throw new System.ArgumentException($"Config variable '{key}' not found.");

            return (string) configMap[key];
        }

        /**
        *  Returns a config integer corresponding to the given @key
        */
        public int GetInt(string key) {
            if (!configMap.Contains(key))
                throw new System.ArgumentException($"Config variable '{key}' not found.");

            return int.Parse((string) configMap[key]);
        }

    }
}