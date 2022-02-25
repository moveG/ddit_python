package day05;

import java.awt.BorderLayout;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JTextField;
import javax.swing.JLabel;
import javax.swing.SwingConstants;
import javax.swing.JButton;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MySwing12_2 extends JFrame {

	private JPanel contentPane;
	private JTextField tf1;
	private JTextField tf2;
	private JTextField tf3;
	private JButton btn1;
	private JButton btn2;
	private JButton btn3;
	private JButton btn4;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing12_2 frame = new MySwing12_2();
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
	public MySwing12_2() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 598, 180);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		tf1 = new JTextField();
		tf1.setHorizontalAlignment(SwingConstants.CENTER);
		tf1.setBounds(12, 10, 116, 21);
		contentPane.add(tf1);
		tf1.setColumns(10);
		
		tf2 = new JTextField();
		tf2.setHorizontalAlignment(SwingConstants.CENTER);
		tf2.setBounds(249, 10, 116, 21);
		contentPane.add(tf2);
		tf2.setColumns(10);
		
		JLabel lbl = new JLabel("=");
		lbl.setHorizontalAlignment(SwingConstants.CENTER);
		lbl.setBounds(391, 13, 40, 15);
		contentPane.add(lbl);
		
		tf3 = new JTextField();
		tf3.setHorizontalAlignment(SwingConstants.CENTER);
		tf3.setBounds(450, 10, 116, 21);
		contentPane.add(tf3);
		tf3.setColumns(10);
		
		btn1 = new JButton("+");
		btn1.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				add();
			}
		});
		btn1.setBounds(140, 9, 97, 23);
		contentPane.add(btn1);
		
		btn2 = new JButton("-");
		btn2.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				minus();
			}
		});
		btn2.setBounds(140, 42, 97, 23);
		contentPane.add(btn2);
		
		btn3 = new JButton("*");
		btn3.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				multiply();
			}
		});
		btn3.setBounds(140, 75, 97, 23);
		contentPane.add(btn3);
		
		btn4 = new JButton("/");
		btn4.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				divide();
			}
		});
		btn4.setBounds(140, 108, 97, 23);
		contentPane.add(btn4);
	}
	
	public void add() {
		String a = tf1.getText();
		String b = tf2.getText();
		float fa = Float.parseFloat(a);
		float fb = Float.parseFloat(b);
		float fc = fa + fb;
		
		tf3.setText(Float.toString(fc));
	}
	
	public void minus() {
		String a = tf1.getText();
		String b = tf2.getText();
		float fa = Float.parseFloat(a);
		float fb = Float.parseFloat(b);
		float fc = fa - fb;
		
		tf3.setText(Float.toString(fc));
	}
	
	public void multiply() {
		String a = tf1.getText();
		String b = tf2.getText();
		float fa = Float.parseFloat(a);
		float fb = Float.parseFloat(b);
		float fc = fa * fb;
		
		tf3.setText(Float.toString(fc));
	}
	
	public void divide() {
		String a = tf1.getText();
		String b = tf2.getText();
		float fa = Float.parseFloat(a);
		float fb = Float.parseFloat(b);
		float fc = fa / fb;
		
		tf3.setText(Float.toString(fc));
	}
}
