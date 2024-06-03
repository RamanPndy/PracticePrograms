public class User{
    
    private String userId;
    private String name;
    private String email;
    private HashMap<User,Double> balances;

    
    public HashMap<User, Double> getBalances() {
        return balances;
    }


    public User(String name, String email) {
        this.name = name;
        this.email = email;
    }


    public void setUserId(String userId) {
        this.userId = userId;
    }


    public String getUserId() {
        return userId;
    }


    public String getName() {
        return name;
    }


    public User(String userId, String name, String email) {
        this.userId = userId;
        this.name = name;
        this.email = email;
        this.balances = new HashMap<>();
    }


    public void setName(String name) {
        this.name = name;
    }


    public String getEmail() {
        return email;
    }


    public void setEmail(String email) {
        this.email = email;
    }

    @Override
    public String toString() {
        return "User [name=" + name + "]";
    }

    @Override
    public boolean equals(Object obj) {
        if(obj instanceof User)
        {
            User givenUser = (User)obj;
            return userId.equals(givenUser.getUserId());
        }
        return false;
    }
}

public class ExpenseGroup {
    
    private double transactionAmount;
    private User giver;
    private List<User> takers;
    private SplitType splittype;

    private HashMap<User,Double> exactSplit;
    private HashMap<User,Integer> percentSplit;

    public double getTransactionAmount() {
        return transactionAmount;
    }
    public ExpenseGroup() {
        this.exactSplit = new HashMap<>();
        this.percentSplit = new HashMap<>();
    }
    public void setTransactionAmount(double transactionAmount) {
        this.transactionAmount = transactionAmount;
    }
    public User getGiver() {
        return giver;
    }
    public void setGiver(User giver) {
        this.giver = giver;
    }
    public List<User> getTakers() {
        return takers;
    }
    public void setTakers(List<User> takers) {
        this.takers = takers;
    }
    public SplitType getSplittype() {
        return splittype;
    }
    public void setSplittype(String splittype) {

        if(splittype.equals("EXACT"))
        {
            this.splittype = new ExactSplitType(this);
        }else if(splittype.equals("PERCENT"))
        {
            this.splittype = new PercentSplitType(this);
        }else if(splittype.equals("EQUAL")) {
            this.splittype = new EqualSplitType(this);
        }else{
            throw new IllegalArgumentException("Invalid splittype given");
        }

        
        Scanner sc = new Scanner(System.in);
        if(this.splittype instanceof ExactSplitType)
        {
            for (User user : takers) {
                System.out.println("Enter exact amount for " + user.getName());
                double nextDoubleInp = sc.nextDouble();
                exactSplit.put(user,nextDoubleInp );
            }
        }else if(this.splittype instanceof PercentSplitType)
        {
            for (User user : takers) {
                System.out.println("Enter percent for " + user.getName());
                int nextIntInp = sc.nextInt();
                
                percentSplit.put(user,nextIntInp);
            }
        }
        // sc.close();
    }

    public HashMap<User, Double> getExactSplit() {
        return exactSplit;
    }
    public void setExactSplit(HashMap<User, Double> exactSplit) {
        this.exactSplit = exactSplit;
    }
    public HashMap<User, Integer> getPercentSplit() {
        return percentSplit;
    }
    public void setPercentSplit(HashMap<User, Integer> percentSplit) {
        this.percentSplit = percentSplit;
    }
    public int getTotalUserInvolvedforExpense()
    {
        return takers.size();
    }

}

public interface SplitType {

    double getPart(User user) throws IllegalExactSplitGiven, IllegalPercentSplitGiven ;
}

public class EqualSplitType implements SplitType{

    ExpenseGroup expenseGroup;

    @Override
    public double getPart(User user) {
        
        int totalPeople = expenseGroup.getTotalUserInvolvedforExpense();
        double txAmount = expenseGroup.getTransactionAmount();

        return txAmount/totalPeople;
    }

    public EqualSplitType(ExpenseGroup expenseGroup) {
        this.expenseGroup = expenseGroup;
    }
}

public class ExactSplitType implements SplitType{

    ExpenseGroup expenseGroup;
    @Override
    public double getPart(User user) throws IllegalExactSplitGiven{
        
        if(getExactSplitSum() != expenseGroup.getTransactionAmount())
        {
            throw new IllegalExactSplitGiven("sum of participants not equal to total tx amount");
        }

        return expenseGroup.getExactSplit().get(user);
    }
    public ExactSplitType(ExpenseGroup expenseGroup) {
        this.expenseGroup = expenseGroup;
    }

    private double getExactSplitSum()
    {
        double givenByUser = 0;
        for (Entry<User,Double> entry: expenseGroup.getExactSplit().entrySet()) {
            givenByUser += entry.getValue();
        }
        return givenByUser;
    }
}

public class PercentSplitType implements SplitType{

    ExpenseGroup expenseGroup;
    @Override
    public double getPart(User user) throws IllegalPercentSplitGiven {
        
        if(!isPercentSplitSumEqualTo100())
        {
            throw new IllegalPercentSplitGiven("total sum of percent does not equal to 100");
        }

        return expenseGroup.getTransactionAmount()*expenseGroup.getPercentSplit().get(user)/100;
    }

    public PercentSplitType(ExpenseGroup expenseGroup) {
        this.expenseGroup = expenseGroup;
    }
    
    private boolean isPercentSplitSumEqualTo100()
    {
        int total = 0;
        for (Entry<User,Integer>entry : expenseGroup.getPercentSplit().entrySet()) {
            total += entry.getValue();
        }

        return total == 100;
    }
}

public class ExpenseManager {
    private ExpenseGroup expenseGroup;

    public ExpenseManager(ExpenseGroup expenseGroup) {
        this.expenseGroup = expenseGroup;
    }


    public void updateBalanceForUser() 
    {
        User giver = expenseGroup.getGiver();
        for (User taker : expenseGroup.getTakers()) {
            try {
                // update taker
                double part = expenseGroup.getSplittype().getPart(taker);
                if(!giver.equals(taker))
                {
                    if(taker.getBalances().containsKey(giver))
                    {
                        double prevAmt = taker.getBalances().get(giver);
                        taker.getBalances().put(giver, prevAmt-part);
                    }else{
                        taker.getBalances().put(giver, -1*part);
                    }
                

                    // update giver
                    if(giver.getBalances().containsKey(taker))
                    {
                        double prevAmt = giver.getBalances().get(taker);
                        giver.getBalances().put(taker, prevAmt + part);
                    }else{
                        giver.getBalances().put(taker, part);
                    }
                }
                
                
            } catch (IllegalExactSplitGiven | IllegalPercentSplitGiven e) {
                
                System.out.println(e.getClass().getName() + " : " + e.getMessage());
            }
        }
    }
    
}

public class IllegalExactSplitGiven extends Exception{

    public IllegalExactSplitGiven(String message) {
        super(message);
    }
    
}

public class IllegalPercentSplitGiven extends Exception{

    public IllegalPercentSplitGiven(String message) {
        super(message);
    }
    
}
