package day04;

import java.awt.BorderLayout;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JTextField;
import javax.swing.JLabel;
import javax.swing.JButton;
import javax.swing.SwingConstants;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MySwing03 extends JFrame {

	private JPanel contentPane;
	private JTextField tf1;
	private JTextField tf2;
	private JTextField tf3;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing03 frame = new MySwing03();
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
	public MySwing03() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 605, 105);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		tf1 = new JTextField();
		tf1.setBounds(12, 20, 116, 21);
		contentPane.add(tf1);
		tf1.setColumns(10);
		
		JLabel lbl = new JLabel("+");
		lbl.setHorizontalAlignment(SwingConstants.CENTER);
		lbl.setBounds(140, 23, 57, 15);
		contentPane.add(lbl);
		
		tf2 = new JTextField();
		tf2.setBounds(209, 20, 116, 21);
		contentPane.add(tf2);
		tf2.setColumns(10);
		
		JButton btn = new JButton("=");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				myClick();
			}
		});
		btn.setBounds(358, 19, 57, 23);
		contentPane.add(btn);
		
		tf3 = new JTextField();
		tf3.setBounds(446, 20, 116, 21);
		contentPane.add(tf3);
		tf3.setColumns(10);
	}
	
	public void myClick() {
		String value1 = tf1.getText();
		String value2 = tf2.getText();
		
		int num1 = Integer.parseInt(value1);
		int num2 = Integer.parseInt(value2);
		
		int result = num1 + num2;
		
		tf3.setText(Integer.toString(result));
	}
}
