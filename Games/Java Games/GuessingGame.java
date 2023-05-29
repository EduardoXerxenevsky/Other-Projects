
import java.util.Random;
import java.util.Scanner;

public class GuessingGame {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        Random random = new Random();
        int numeroAleatorio = random.nextInt(101);
        int tentativas = 0;
        int palpite = 0;

        System.out.println("Bem-vindo ao jogo de adivinhação!");
        System.out.println("Estou pensando em um número entre 1 e 100...");
        
        while (palpite != numeroAleatorio) {
            System.out.println("Qual é o seu palpite? ");
            palpite = input.nextInt();
            tentativas++;

            if (palpite < numeroAleatorio) {
                System.out.println("O número que estou pensando é maior do que " + palpite + ".");
            } else if (palpite > numeroAleatorio) {
                System.out.println("O número que estou pensando é menor do que " + palpite + ".");
            } else {
                System.out.println("É " + numeroAleatorio + " !!!");
            }
        }
    }
}