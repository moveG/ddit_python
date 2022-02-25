package day05;

import java.awt.BorderLayout;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JTextField;
import javax.swing.JLabel;
import javax.swing.JButton;
import javax.swing.SwingConstants;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MySwing09 extends JFrame {

	private JPanel contentPane;
	private JTextField tf1;
	private JTextField tf2;
	private JTextField tf3;
	private JTextField tf4;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing09 frame = new MySwing09();
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
	public MySwing09() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 790, 81);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		tf1 = new JTextField();
		tf1.setBounds(12, 10, 116, 21);
		contentPane.add(tf1);
		tf1.setColumns(10);
		
		JLabel lbl1 = new JLabel("에서");
		lbl1.setHorizontalAlignment(SwingConstants.CENTER);
		lbl1.setBounds(140, 13, 57, 15);
		contentPane.add(lbl1);
		
		tf2 = new JTextField();
		tf2.setBounds(209, 10, 116, 21);
		contentPane.add(tf2);
		tf2.setColumns(10);
		
		JLabel lbl2 = new JLabel("까지");
		lbl2.setHorizontalAlignment(SwingConstants.CENTER);
		lbl2.setBounds(337, 13, 57, 15);
		contentPane.add(lbl2);
		
		tf3 = new JTextField();
		tf3.setBounds(406, 10, 116, 21);
		contentPane.add(tf3);
		tf3.setColumns(10);
		
		JButton btn = new JButton("배수의 합");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				myClick();
			}
		});
		btn.setBounds(534, 9, 97, 23);
		contentPane.add(btn);
		
		tf4 = new JTextField();
		tf4.setBounds(643, 10, 116, 21);
		contentPane.add(tf4);
		tf4.setColumns(10);
	}
	
	public void myClick() {
		int num1 = Integer.parseInt(tf1.getText());
		int num2 = Integer.parseInt(tf2.getText());
		int num3 = Integer.parseInt(tf3.getText());
		
		int sum = 0; 
		
		for(int i = num1; i <= num2; i++) {
			if(i % num3 == 0) {
				sum += i;
			}
		}
		tf4.setText(Integer.toString(sum));
	}
}
