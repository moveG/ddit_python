package day04;

import java.awt.BorderLayout;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JTextField;
import javax.swing.JButton;
import javax.swing.JTextArea;
import javax.swing.SwingConstants;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;

public class MySwing07 extends JFrame {

	private JPanel contentPane;
	private JTextField tf;
	private JTextArea ta;
	
	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing07 frame = new MySwing07();
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
	public MySwing07() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 229, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lbl = new JLabel("단수");
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
		tf.setBounds(81, 7, 116, 21);
		contentPane.add(tf);
		tf.setColumns(10);
		
		JButton btn = new JButton("출력하기");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				myClick();
			}
		});
		btn.setBounds(12, 35, 185, 23);
		contentPane.add(btn);
		
		ta = new JTextArea();
		ta.setBounds(12, 68, 185, 183);
		contentPane.add(ta);
	}
	public void myClick() {
		String value = tf.getText();
		int num = Integer.parseInt(value);
//		String gugudan = "";
//		for(int i = 1; i <= 9; i++) {
//			gugudan += value + " * " + i + " = " + (num * i) + "\n"; 
//		}
		String gugudan = "";
		gugudan += num + " * 1 = " + (num * 1) + "\n";
		gugudan += num + " * 2 = " + (num * 2) + "\n";
		gugudan += num + " * 3 = " + (num * 3) + "\n";
		gugudan += num + " * 4 = " + (num * 4) + "\n";
		gugudan += num + " * 5 = " + (num * 5) + "\n";
		gugudan += num + " * 6 = " + (num * 6) + "\n";
		gugudan += num + " * 7 = " + (num * 7) + "\n";
		gugudan += num + " * 8 = " + (num * 8) + "\n";
		gugudan += num + " * 9 = " + (num * 9);
		
		ta.setText(gugudan);
	}
}
