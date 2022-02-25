package day05;

import java.awt.BorderLayout;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JTextField;
import javax.swing.JButton;
import javax.swing.JTextArea;
import javax.swing.SwingConstants;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;

public class MySwing11 extends JFrame {

	private JPanel contentPane;
	private JTextField tf;
	private JTextArea ta;
	String com3 = "";

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing11 frame = new MySwing11();
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
	public MySwing11() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 259, 446);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lbl = new JLabel("3number");
		lbl.setBounds(12, 10, 57, 15);
		contentPane.add(lbl);
		
		tf = new JTextField();
		tf.addKeyListener(new KeyAdapter() {
			@Override
			public void keyPressed(KeyEvent e) {
				if(e.getKeyCode() == 10) {
					myClick();
				}
			}
		});
		tf.setHorizontalAlignment(SwingConstants.CENTER);
		tf.setBounds(81, 7, 146, 21);
		contentPane.add(tf);
		tf.setColumns(10);
		
		JButton btn = new JButton("맞추기");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				myClick();
			}
		});
		btn.setBounds(12, 35, 215, 23);
		contentPane.add(btn);
		
		ta = new JTextArea();
		ta.setBounds(12, 68, 215, 321);
		contentPane.add(ta);
		
		com3 = getCom3();
	}
	
	public String getCom3() {
		String[] arr9= {"1", "2", "3", "4", "5", "6", "7", "8", "9"};
		
		for(int i = 0; i < 1000; i++) {
			int rnd = (int) (Math.random() * arr9.length);
			
			String a =arr9[rnd]; 
			String b =arr9[0]; 
			
			arr9[0] = a;
			arr9[rnd] = b;
		}
		
		String ret = arr9[0] + arr9[1] + arr9[2];
		System.out.println("ret : " + ret);
		
		return ret;
	}
	
	public int getS(String mine3) {
		int cnt = 0;
		
		String c1 = com3.substring(0, 1);
		String c2 = com3.substring(1, 2);
		String c3 = com3.substring(2, 3);
		
		String m1 = mine3.substring(0, 1);
		String m2 = mine3.substring(1, 2);
		String m3 = mine3.substring(2, 3);
		
		if(c1.equals(m1)) cnt++;
		if(c2.equals(m2)) cnt++;
		if(c3.equals(m3)) cnt++;
		
		return cnt;
	}
	
	public int getB(String mine3) {
		int cnt = 0;
		
		String c1 = com3.substring(0, 1);
		String c2 = com3.substring(1, 2);
		String c3 = com3.substring(2, 3);
		
		String m1 = mine3.substring(0, 1);
		String m2 = mine3.substring(1, 2);
		String m3 = mine3.substring(2, 3);
		
		if(c1.equals(m2) || c1.equals(m3)) cnt++;
		if(c2.equals(m1) || c2.equals(m3)) cnt++;
		if(c3.equals(m1) || c3.equals(m2)) cnt++;
		
		return cnt;
	}
	
	public void myClick() {
		String mine3 = tf.getText();
		
		int s = getS(mine3);
		int b = getB(mine3);
		
		String str_new = s + "S " + b + "B..." + mine3 + "\n";
		String str_old = ta.getText();
		
		ta.setText(str_new + str_old);
		
		if(s == 3) {
			JOptionPane.showMessageDialog(null, "이겼습니다.");
		}
	}
}
