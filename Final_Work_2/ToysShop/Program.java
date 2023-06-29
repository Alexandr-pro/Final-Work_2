
public class Program {

    public static void main(String[] args) {
        Store s = new Store();
        boolean flag = true;
        while (flag) {
            String inputData = InOut.Input("Enter:\n" +
                    "add - Add a toy to the store\n" +
                    "get - Raffle toys\n" +
                    "shop - Show the assortment\n" +
                    "exit - Exit\n" + ": ");
            System.out.println();
            inputData.toLowerCase();
            switch (inputData) {
                case "add":
                    s.AddToy(new Toy(InOut.Input("Enter the name of toy and the probability: ")));
                    break;
                case "get":
                    s.GetResult(Integer.parseInt(InOut.Input("Enter the number of attempts: ")));
                    System.out.println(s.resultToString());
                    InOut.Save("result.txt", s.resultToString());
                    break;
                case "shop":
                    s.ShowToys();
                    break;
                case "exit":
                    flag = false;
                    break;
                default:
                    System.out.println("Invalid command!");
                    break;
            }
            System.out.println();
        }

    }
}