import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

public class InOut {
    static String Input(String text){
        Scanner in = new Scanner(System.in);
        System.out.print(text);
        return in.nextLine();
    }

    static void Save(String path, String data){
        try(FileWriter writer = new FileWriter(path, false))
        {
            writer.write(data);             
            writer.flush();
        }
        catch(IOException ex){
             
            System.out.println(ex.getMessage());
        } 
    }
}
