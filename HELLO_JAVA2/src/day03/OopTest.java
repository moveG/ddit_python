package day03;

public class OopTest {
	public static void main(String[] args) {
		Human a = new Human();
		
		System.out.println(a.age);
		System.out.println(a.skill_lang);
		a.getOld();
		a.getOld();
		a.mimic();
		System.out.println(a.age);
		System.out.println(a.skill_lang);
	}
}
