import java.util.ArrayList;
import java.util.Comparator;
import java.util.PriorityQueue;

public class Store {
    ArrayList<Toy> toys;
    PriorityQueue<Toy> toyQueue;
    ArrayList<Toy> result;

    public Store() {
        this.toys = new ArrayList<Toy>();
        this.toyQueue = new PriorityQueue<>(
                new Comparator<Toy>() {
                    @Override
                    public int compare(Toy t1, Toy t2) {
                        return Float.compare(t1.GetChance(), t2.GetChance());
                    }
                });
        this.result = new ArrayList<Toy>();
    }

    public void AddToy(Toy toy) {
        toys.add(toy);
    }

    public void ShowToys() {
        for (Toy toy : toys) {
            System.out.println(toy);
        }
    }

    private void CreateQueue() {
        toyQueue.clear();
        float tmpChanceSum = 0;
        for (Toy toy : toys) {
            tmpChanceSum += toy.GetChance();
        }
        for (Toy toy : toys) {
            int tmpCountToy = (int) ((toy.GetChance() / tmpChanceSum) * 100);
            for (int i = 0; i < tmpCountToy; i++) {
                toyQueue.add(toy);
            }
        }
    }

    public void PrintQueue() {
        CreateQueue();
        for (Toy toy : toyQueue) {
            System.out.println(toy);
        }
    }

    public Toy GetToy() {
        CreateQueue();
        int rand = (int) (Math.random() * toyQueue.size());
        for (int i = 1; i < rand; i++) {
            toyQueue.poll();
        }
        return toyQueue.poll();
    }

    public ArrayList<Toy> GetResult(int count) {
        result.clear();
        for (int i = 0; i < count; i++) {
            result.add(GetToy());
        }
        return result;
    }

    public String resultToString() {
        String data = "";
        for (Toy toy : result) {
            data += toy.toString() + "\n";
        }
        return data;
    }
}
