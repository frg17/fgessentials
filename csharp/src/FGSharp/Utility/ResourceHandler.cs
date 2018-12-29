using System;
using System.IO;
using System.Collections;

/*
    Class for easy access to resource files.
*/
namespace FGSharp.Utility {
    
    public class ResourceHandler {
        private string pathPrefix; //Path to directory containing resource directory.
        private string pathDirectory; //Name of resource directory.


        public ResourceHandler() {
            this.pathPrefix = ".";
            pathDirectory = null;
            lookForResourceDirectory();
        }

        public ResourceHandler(string pathPrefix) {
            this.pathPrefix = pathPrefix;
            pathDirectory = null;
            lookForResourceDirectory();
        }
        
        /**
        * Looks for a resource folder in the given directory.
        * Throws an exception if no such directory is found.
        */
        private void lookForResourceDirectory() {
            if (Directory.Exists($"{pathPrefix}/res"))
                pathDirectory = "res";

            if (Directory.Exists($"{pathPrefix}/resources"))
                pathDirectory = "resources";
            
            if(pathDirectory == null) {
                throw new FileNotFoundException("No resource folder found.");
            }
        }

        /**
        * Retrieves config file and returns all properties in a hashtable.
        */
        public Hashtable GetConfig() {
            Hashtable configMap = new Hashtable();
            //Read file.
            string text = File.ReadAllText($"{pathPrefix}/{pathDirectory}/app.conf");
            String[] lines = text.Split("\n");

            //Strip file.
            foreach(string l in lines) {
                if(!String.IsNullOrEmpty(l)) {
                    string[] key_val = l.Split("=");
                    if(key_val.Length != 2) {
                        throw new ArgumentException("Error reading app.conf");
                    } else {
                        configMap.Add(key_val[0], key_val[1]);
                    }
                }
            }
            
            return configMap;
        }
    }
}