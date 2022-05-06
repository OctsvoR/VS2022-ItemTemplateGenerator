# VS2022-UnityItemTemplateGenerator

A Python program that generates Visual Studio 2022 Unity C# item template.

**Warning! This program is very unstable, which is very likely to cause some errors. Please use with caution!**

## How to use:
1. Place the **"gen.py"**, **"icon.ico"**, and **"SyntaxTree.VisualStudio.Unity.Vsix.Item..vstman"** into **"...\Microsoft Visual Studio\2022\Community\Common7\IDE\Extensions\Microsoft\Visual Studio Tools for Unity\ItemTemplates"** folder
2. Run the **"gen.py"** as administrator
3. Input the item template name
4. Edit the **"CSharp/1033/CSharp [item template name]/New[item template name].cs"** file with a text editor
5. Fill in anything you want for the code to be generated, and put in "$safeitemname$" for the class name
6. Done
