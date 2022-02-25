package day04;

import java.awt.BorderLayout;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JTextField;
import javax.swing.JButton;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import javax.swing.SwingConstants;

public class MySwing08 extends JFrame {

	private JPanel contentPane;
	private JTextField tf;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing08 frame = new MySwing08();
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
	public MySwing08() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 218, 284);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		tf = new JTextField();
		tf.setHorizontalAlignment(SwingConstants.RIGHT);
		tf.setBounds(12, 10, 177, 37);
		contentPane.add(tf);
		tf.setColumns(10);
		
		JButton btn1 = new JButton("1");
		btn1.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				JButton obj = (JButton) e.getSource();
				myClick(obj.getText());
			}
		});
		btn1.setBounds(12, 151, 51, 37);
		contentPane.add(btn1);
		
		JButton btn2 = new JButton("2");
		btn2.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				JButton obj = (JButton) e.getSource();
				myClick(obj.getText());
			}
		});
		btn2.setBounds(75, 151, 51, 37);
		contentPane.add(btn2);
		
		JButton btn3 = new JButton("3");
		btn3.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				JButton obj = (JButton) e.getSource();
				myClick(obj.getText());
			}
		});
		btn3.setBounds(138, 151, 51, 37);
		contentPane.add(btn3);
		
		JButton btn4 = new JButton("4");
		btn4.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				JButton obj = (JButton) e.getSource();
				myClick(obj.getText());
			}
		});
		btn4.setBounds(12, 104, 51, 37);
		contentPane.add(btn4);
		
		JButton btn5 = new JButton("5");
		btn5.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				JButton obj = (JButton) e.getSource();
				myClick(obj.getText());
			}
		});
		btn5.setBounds(75, 104, 51, 37);
		contentPane.add(btn5);
		
		JButton btn6 = new JButton("6");
		btn6.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				JButton obj = (JButton) e.getSource();
				myClick(obj.getText());
			}
		});
		btn6.setBounds(138, 104, 51, 37);
		contentPane.add(btn6);
		
		JButton btn7 = new JButton("7");
		btn7.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				JButton obj = (JButton) e.getSource();
				myClick(obj.getText());
			}
		});
		btn7.setBounds(12, 57, 51, 37);
		contentPane.add(btn7);
		
		JButton btn8 = new JButton("8");
		btn8.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				JButton obj = (JButton) e.getSource();
				myClick(obj.getText());
			}
		});
		btn8.setBounds(75, 57, 51, 37);
		contentPane.add(btn8);
		
		JButton btn9 = new JButton("9");
		btn9.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				JButton obj = (JButton) e.getSource();
				myClick(obj.getText());
			}
		});
		btn9.setBounds(138, 57, 51, 37);
		contentPane.add(btn9);
		
		JButton btn0 = new JButton("0");
		btn0.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				JButton obj = (JButton) e.getSource();
				myClick(obj.getText());
			}
		});
		btn0.setBounds(12, 198, 51, 37);
		contentPane.add(btn0);
		
		JButton btnCall = new JButton("Call");
		btnCall.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				myAlert();	
			}
		});
		btnCall.setBounds(75, 198, 114, 37);
		contentPane.add(btnCall);
	}
	
	public void myAlert() {
		String tel = tf.getText();
		
		JOptionPane.showMessageDialog(null, tel);
	}
	
	public void myClick(String num_new) {
		String num_old = tf.getText();
		
		num_old += num_new;
		
		tf.setText(num_old);
	}
}
