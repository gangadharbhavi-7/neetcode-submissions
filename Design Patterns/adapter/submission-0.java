// Existing classes
class Square {
    private double side;

    public Square(double side) {
        this.side = side;
    }

    public double getSide() {
        return side;
    }
}

class SquareHole {
    private double length;

    public SquareHole(double length) {
        this.length = length;
    }

    public boolean canFit(Square square) {
        return square.getSide() <= length;
    }
}

class Circle {
    private double radius;

    public Circle(double radius) {
        this.radius = radius;
    }

    public double getRadius() {
        return radius;
    }
}

// Adapter: Circle → Square
class CircleToSquareAdapter extends Square {
    private Circle circle;

    public CircleToSquareAdapter(Circle circle) {
        // Call parent constructor with equivalent "side"
        super(circle.getRadius() * 2);  // diameter = 2 * radius
        this.circle = circle;
    }
}
