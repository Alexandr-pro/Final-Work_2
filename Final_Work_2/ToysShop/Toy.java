
public class Toy {
    static int counter = 0;
    private int id;
    private float chance;
    private String name;

    Toy(String name, float chance){
        this.id = ++counter;
        this.chance = chance;
        this.name = name;
    }

    Toy(String data){
        String str = data.trim();
        String[] tmp = str.split(" ");
        this.id = ++counter;
        this.chance = Float.parseFloat(tmp[1]);
        this.name = tmp[0];
    }

    int GetId(){ return this.id; }
    float GetChance(){ return this.chance;}
    String GetName(){ return this.name;}

    @Override
    public String toString() {
        return "ID:" + this.id + " | " + this.name + " | Chance: " + this.chance;
    }
}
