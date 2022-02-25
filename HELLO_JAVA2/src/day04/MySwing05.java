package day04;

import java.awt.BorderLayout;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JButton;
import javax.swing.SwingConstants;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.util.ArrayList;
import java.util.List;
import java.util.Set;
import java.util.TreeSet;

public class MySwing05 extends JFrame {

	private JPanel contentPane;
	JLabel lbl1;
	JLabel lbl2;
	JLabel lbl3;
	JLabel lbl4;
	JLabel lbl5;
	JLabel lbl6;
	
	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing05 frame = new MySwing05();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the frame.
	 */
	public MySwing05() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 499, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		lbl1 = new JLabel("__");
		lbl1.setHorizontalAlignment(SwingConstants.CENTER);
		lbl1.setBounds(34, 34, 57, 15);
		contentPane.add(lbl1);
		
		lbl3 = new JLabel("__");
		lbl3.setHorizontalAlignment(SwingConstants.CENTER);
		lbl3.setBounds(172, 34, 57, 15);
		contentPane.add(lbl3);
		
		lbl5 = new JLabel("__");
		lbl5.setHorizontalAlignment(SwingConstants.CENTER);
		lbl5.setBounds(310, 34, 57, 15);
		contentPane.add(lbl5);
		
		lbl2 = new JLabel("__");
		lbl2.setHorizontalAlignment(SwingConstants.CENTER);
		lbl2.setBounds(103, 34, 57, 15);
		contentPane.add(lbl2);
		
		lbl4 = new JLabel("__");
		lbl4.setHorizontalAlignment(SwingConstants.CENTER);
		lbl4.setBounds(241, 34, 57, 15);
		contentPane.add(lbl4);
		
		lbl6 = new JLabel("__");
		lbl6.setHorizontalAlignment(SwingConstants.CENTER);
		lbl6.setBounds(379, 34, 57, 15);
		contentPane.add(lbl6);
		
		JButton btn = new JButton("로또자동생성");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				myClick();
			}
		});
		btn.setBounds(34, 88, 402, 23);
		contentPane.add(btn);
	}
	
	public void myClick() {
//		int[] num = new int[45];
//		for(int i = 0; i < 45; i++) {
//			num[i] = i + 1;
//		}
//		
//		int[] lotto = new int[6];
//		
//		for(int i = 0; i < 6; i++) {
//			lotto[i] = (int)(Math.random() * 45) + 1;
//			
//			if(i > 0) {
//				for(int j = 0; j < i; j++) {
//					while(lotto[i] == lotto[j]) {
//						lotto[i] = (int)(Math.random() * 45) + 1;
//					}
//				}
//			}
//		}
//		
//		lbl1.setText(Integer.toString(lotto[0]));
//		lbl2.setText(Integer.toString(lotto[1]));
//		lbl3.setText(Integer.toString(lotto[2]));
//		lbl4.setText(Integer.toString(lotto[3]));
//		lbl5.setText(Integer.toString(lotto[4]));
//		lbl6.setText(Integer.toString(lotto[5]));
		
//		Set<Integer> lotto = new TreeSet<Integer>();
//		
//		while(true) {
//			int rnd = (int)(Math.random() * 45) + 1;
//			lotto.add(rnd);
//			
//			if(lotto.size() >= 6) {
//				break;
//			}
//		}
//		
//		List<Integer> list = new ArrayList<Integer>(lotto);
//		
//		lbl1.setText(Integer.toString(list.get(0)));
//		lbl2.setText(Integer.toString(list.get(1)));
//		lbl3.setText(Integer.toString(list.get(2)));
//		lbl4.setText(Integer.toString(list.get(3)));
//		lbl5.setText(Integer.toString(list.get(4)));
//		lbl6.setText(Integer.toString(list.get(5)));
		
		String[] arr45 = {
			 "1",  "2",  "3",  "4",  "5",  "6",  "7",  "8",  "9", "10", 
			"11", "12", "13", "14", "15", "16", "17", "18", "19", "20", 
			"21", "22", "23", "24", "25", "26", "27", "28", "29", "30", 
			"31", "32", "33", "34", "35", "36", "37", "38", "39", "40",				
			"41", "42", "43", "44", "45"
		};
		
		for(int i = 0; i < 10000; i++) {
			int rnd = (int) (Math.random() * arr45.length);
			
			String a = arr45[0];
			String b = arr45[rnd];
			
			arr45[0] = b;
			arr45[rnd] = a;
		}
		
		lbl1.setText(arr45[0]);
		lbl2.setText(arr45[1]);
		lbl3.setText(arr45[2]);
		lbl4.setText(arr45[3]);
		lbl5.setText(arr45[4]);
		lbl6.setText(arr45[5]);
		
	}
}
