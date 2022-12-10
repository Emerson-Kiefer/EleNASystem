import javax.swing.*;
import java.awt.*;


public class MainFrame extends JFrame{
    final private Font mainFont = new Font("Aerial", Font.BOLD, 18);
    JTextField JTForigin_field, JTFdest_field, JTFdist_field;

    public void initialize(){
        JLabel JLorigin = new JLabel("Origin: ");
        JLorigin.setFont(mainFont);

        JLabel JLdestination = new JLabel("Destination: ");
        JLdestination.setFont(mainFont);

        JLabel JLdistance = new JLabel("% Distance: ");
        JLdistance.setFont(mainFont);

        JTForigin_field = new JTextField();
        JTForigin_field.setFont(mainFont);

        JTFdist_field = new JTextField();
        JTFdist_field.setFont(mainFont);

        JTFdest_field = new JTextField();
        JTFdist_field.setFont(mainFont);

        JPanel formPanel = new JPanel();
        formPanel.setLayout(new GridLayout(4, 1, 5, 5));
        formPanel.add(JLorigin);
        formPanel.add(JTForigin_field);

        formPanel.add(JLdestination);
        formPanel.add(JTFdest_field);

        formPanel.add(JLdistance);
        formPanel.add(JTFdist_field);



        JPanel mainPanel = new JPanel();
        mainPanel.setLayout(new BorderLayout());
        mainPanel.setBackground(new Color(128, 128, 255));
        mainPanel.add(formPanel, BorderLayout.NORTH);
        
        //add mainPanel to Jframe
        add(mainPanel);

        setTitle("Elena Project CS 520");
        setSize(500,600);
        setMinimumSize(new Dimension (300, 400));
        setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
        setVisible(true);
    }

    public static void main (String[] args){
        MainFrame myFrame = new MainFrame();
        myFrame.initialize();
    }
}
